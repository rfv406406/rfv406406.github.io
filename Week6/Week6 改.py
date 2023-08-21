#初始化Flask伺服器
from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect

app=Flask(
    __name__,
    static_folder= "templates",
    static_url_path= "/",
)
app.secret_key= "any string but secret"

import mysql.connector

con=mysql.connector.connect(
    user= "root",
    password= "rfv406406",
    host= "127.0.0.1",
    database= "website"
)

#處理路由
@app.route("/")
def index():
    return render_template("Week6.html")

@app.route("/member")
def member():
    if "name" in session and "username" in session and "password" in session:
        cursor= con.cursor()
        cursor.execute("SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id")
        data= cursor.fetchall()
        cursor.close()
        # result=""
        # for row in data:
        #     membername= row[0]
        #     messagecontent= row[1]
        #     result += membername+":"+messagecontent+ "\n" 
        return render_template("Week6member.html", message= session["name"], messages= data)
    else:
        return redirect("/")

# /error?msg=錯誤訊息
@app.route("/error")
def error():
    message= request.args.get("message","")
    return render_template("Week6error.html", message= message)

@app.route("/signup", methods= ["POST"])
def signup():
  
    name= request.form["name"]
    username= request.form["username"]
    password= request.form["password"]

    cursor= con.cursor()
    cursor.execute("SELECT username FROM member WHERE username= %s", (username, ))
    data= cursor.fetchone()
    if data is None:
        cursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)", (name, username, password)) 
        con.commit() #執行
        cursor.close()
        return render_template("Week6.html")
    else:
        cursor.close()
        return redirect("/error?message=帳號已被註冊")


@app.route("/signin", methods=["POST"])
def signin():
    #從前端取得使用者輸入
    Username= request.form["Username"]
    Password= request.form["Password"]

    cursor= con.cursor()
    cursor.execute("SELECT name, username, password FROM member WHERE username= %s", (Username, ))
    data= cursor.fetchone()
    cursor.close() 

    if data and data[2]== Password:
        session["name"]= data[0]
        session["username"]= data[1]
        session["password"]= data[2]
        
        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    
@app.route("/createMessage", methods=["POST"])
def createMessage():
    
    Message= request.form["Message"]

    if Message== "":
        return redirect("/member")
    if "username" in session:
        username= session["username"]
        cursor= con.cursor()
        cursor.execute("SELECT id FROM member WHERE username= %s", (username, ))
        data= cursor.fetchone()
        if data:
            member_id =data[0]
            cursor.execute("INSERT INTO message (member_id, content) VALUES(%s, %s)", (member_id, Message, )) 
            con.commit() 
            cursor.close()
            return redirect("/member")

@app.route("/signout")
def signout():
    #移除會員資訊
    session.pop("name", None)
    session.pop("username", None)
    session.pop("password", None)

    return redirect("/")
#啟動伺服器
app.run(port=3000)