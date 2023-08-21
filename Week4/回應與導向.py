from flask import Flask #載入Flask
from flask import request
from flask import redirect
import json

#建立Application物件
app=Flask(__name__,
          static_folder="static",
          static_url_path="/"
          ) 
# 建立路徑/en/對應的處理函式
@app.route("/en/") 
def index_english():
    return json.dumps({
        "status":"OK",
        "text":"Hello World"
    })
 
# 建立路徑/zh/對應的處理函式
@app.route("/zh/") 
def index_chinese():
    return json.dumps({
        "status":"OK",
        "text":"您好"
    } , ensure_ascii=False)

#建立路徑/對應的處理函式
@app.route("/") #函式的裝飾(decorator):已函式為基礎，提供附加功能。
def index(): #用來回應路徑/的函式

    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
    else:
        return redirect("/zh/")

#啟動網站伺服器,可透過port指定埠號
    app.run(port=3000)