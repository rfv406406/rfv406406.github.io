#初始化資料庫連線
# import pymongo
# client=pymongo.MongoClient("連線網址")
# db=client.member_system

#初始化Flask伺服器
from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/",
)
app.secret_key="any string but secret"
#處理路由
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")

# /error?msg=錯誤訊息
@app.route("/error")
def error():
    msg=request.args.get("msg","發生錯誤，請聯繫克服")
    return render_template("error.html", message = message)

@app.route("/signin", method=["POST"])
def sigein():
    #從前端取得使用者輸入
    email=request.form["email"]
    password=request.form["password"]

#找不到登入資料，登入失敗
if result == None:
    return redirect("/error?msg=帳號或密碼輸入錯誤")
session["nickname"]=result["nickname"]
return redirect("/member")

@app.route("/signout")
def signout():
    #移除會員資訊
    del session["nickname"]
    return redirect("/")
#啟動伺服器
app.run(port=3000)