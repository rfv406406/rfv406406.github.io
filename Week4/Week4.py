#初始化資料庫連線
# import pymongo
# client=pymongo.MongoClient("連線網址")
# db=client.member_system

#初始化Flask伺服器
from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect

app=Flask(
    __name__,
    static_folder="templates",
    static_url_path="/",
)
app.secret_key="any string but secret"
#處理路由
@app.route("/")
def index():
    return render_template("Week4.html")

@app.route("/member")
def member():
    if "account" in session and "password" in session:
        return render_template("Week4member.html")
    else:
        return redirect("/")

# /error?msg=錯誤訊息
@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("Week4error.html", message = message)
    

@app.route("/signin", methods=["POST"])
def signin():
    #從前端取得使用者輸入
    account=request.form["account"]
    password=request.form["password"]
    #找不到登入資料，登入失敗
    if account == ""  or password == "":
        return redirect("/error?message=請輸入帳號密碼")
    if account != "test" or password != "test":
        return redirect("/error?message=帳號、或密碼錯誤")
    
    session["account"]=account
    session["password"]=password
    return redirect("/member")

@app.route("/signout")
def signout():
    #移除會員資訊
    del session["account"]  
    del session["password"]
    return redirect("/")
# 啟動伺服器
app.run(port=3000)