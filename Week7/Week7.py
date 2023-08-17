#初始化Flask伺服器
from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
import json

app = Flask(
    __name__,
    static_folder= "templates",
    static_url_path= "/",
)
app.secret_key = "any string but secret"

import mysql.connector

con=mysql.connector.connect(
    user = "root",
    password = "rfv406406",
    host = "127.0.0.1",
    database = "website"
)

#處理路由
@app.route("/")
def index():
    return render_template("Week7.html")

@app.route("/member")
def member():
    if "name" in session and "username" in session and "password" in session:
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id")
        data = cursor.fetchall()
        
        messages = ""  
        for row in data:
            message_str = "{}:{}\n".format(row["name"], row["content"])  
            messages += message_str 
        
        cursor.close()

        return render_template("Week7member.html", message = session["name"], messages = messages)
    else:
        return redirect("/")

@app.route("/api/member", methods=["GET","PATCH"])
def api_member():
    if request.method == "GET":
        if "name" in session and "username" in session and "password" in session:
            username = request.args.get("username")
            cursor = con.cursor(dictionary = True)
            cursor.execute("SELECT id, name, username FROM member WHERE username = %s", (username,))
            result = cursor.fetchall()
            cursor.close()
            if result:
                name_dict = {
                    "data": result
                }
            else:
                name_dict = {
                    "data": None
                }
            json_name_dict = json.dumps(name_dict)
            return json_name_dict
        else:
            name_dict = {
                "data": None
            }
            json_name_dict = json.dumps(name_dict)
            return json_name_dict
            
    if request.method == "PATCH":
        if "name" in session and "username" in session and "password" in session:

            data = request.json
            renew_name = data.get("name")
            cursor = con.cursor(dictionary=True)
            cursor.execute("UPDATE member SET name = %s WHERE username = %s", (renew_name, session["username"]))
            con.commit()
            cursor.execute("SELECT id, name, username FROM member WHERE username = %s", (session["username"],))
            result = cursor.fetchone()
            cursor.close()
            if result and result["name"] == renew_name:
                session["name"] = renew_name
                return '{"ok": true}'
            else:
                return '{"error": true}'
        else:
            return '{"error": true}'

# /error?msg=錯誤訊息
@app.route("/error")
def error():
    message = request.args.get("message","")
    return render_template("Week7error.html", message = message)

@app.route("/signup", methods = ["POST"])
def signup():
  
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    cursor = con.cursor()
    cursor.execute("SELECT username FROM member WHERE username= %s", (username, ))
    data = cursor.fetchone()
    if data is None:
        cursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)", (name, username, password)) 
        con.commit() #執行
        cursor.close()
        return render_template("Week7.html")
    else:
        cursor.close()
        return redirect("/error?message=帳號已被註冊")


@app.route("/signin", methods = ["POST"])
def signin():
    #從前端取得使用者輸入
    Username = request.form["Username"]
    Password = request.form["Password"]

    cursor = con.cursor()
    cursor.execute("SELECT name, username, password FROM member WHERE username= %s", (Username, ))
    data = cursor.fetchone()
    cursor.close() 

    if data and data[2] == Password:
        session["name"] = data[0]
        session["username"] = data[1]
        session["password"] = data[2]
        
        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    
@app.route("/createMessage", methods = ["POST"])
def createMessage():
    
    Message = request.form["Message"]

    if Message == "":
        return redirect("/member")
    if "username" in session:
        username = session["username"]
        cursor = con.cursor()
        cursor.execute("SELECT id FROM member WHERE username= %s", (username, ))
        data = cursor.fetchone()
        if data:
            member_id = data[0]
            cursor.execute("INSERT INTO message (member_id, content) VALUES(%s, %s)", (member_id, Message, )) 
            con.commit() 
            cursor.close()
            return redirect("/member")
        
# @app.route("/deleteMessage", methods = ["POST"])
# def deleteMessage():
    
#     message = request.form["message"]

#     if "username" in session:
#         username = session["username"]
#         cursor = con.cursor()
#         cursor.execute("SELECT id FROM member WHERE username= %s", (username, ))
#         data = cursor.fetchone()
#         if data:
#             member_id = data[0]
#             cursor.execute("INSERT INTO message (member_id, content) VALUES(%s, %s)", (member_id, Message, )) 
#             con.commit() 
#             cursor.close()
#             return redirect("/member")

@app.route("/signout")
def signout():
    #移除會員資訊
    session.pop("name", None)
    session.pop("username", None)
    session.pop("password", None)

    return redirect("/")
#啟動伺服器
app.run(port=3000)
