from flask import Flask
from flask import request
from flask import render_template
from flask import session  

app=Flask(__name__,static_Floder="static", static_url_path="/")

#設定Session密鑰
app.secret_key="any string but secret"

#使用GET,處裡路徑/的對應函式
@app.route("/")
def index1():
    return render_template("index1.html")

@app.route("/hello")
def hello():
    name=request.args.get("name", "")
    session["username"]=name #session["欄位名稱"]=資料
    return "你好"+ name

@app.route("/talk")
def talk():
    name=session["username"]
    return name + "高興見到你"


#啟動網站伺服器,可透過port參數設定埠號
app.run(port=3000)