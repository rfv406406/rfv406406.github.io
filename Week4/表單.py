from flask import Flask
from flask import request
form flask import render_template  

app=Flask(__name__,static_Floder="static", static_url_path="/")

#處裡路徑/的對應函式
@app.route("/")
def index1():
    return render_template("index1.html")

@app.route("/calculate")
def calculate():
    maxNumber=request.args.get("max", "")
    maxNumber=int(maxNumber)
    # 1+2+3+...+maxNumber
    result=0
    for n in range(1, maxNumber+1):
        result+=n
    return render_template("result.html", data=str(result)) #不佳也可自動轉換字串

@app.route("/")
def show():
    return "歡迎光臨," + name

@app.route("/page")
def page():
    return render_template("page.html")
#啟動網站伺服器,可透過port參數設定埠號
app.run(port=3000)