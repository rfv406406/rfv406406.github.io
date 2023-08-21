from flask import Flask
from flask import request
form flask import render_template  

app=Flask(__name__,static_Floder="static", static_url_path="/")

#處裡路徑/的對應函式
@app.route("/")
def index1():
    return render_template("index1.html")

@app.route("/page")
def page():
    return render_template("page.html")
#啟動網站伺服器,可透過port參數設定埠號
app.run(port=3000)