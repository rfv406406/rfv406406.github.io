from flask import Flask #載入Flask

app=Flask(__name__) #建立Application物件

#建立網站首頁回應方式
@app.route("/") #函式的裝飾(decorator):已函式為基礎，提供附加功能。
def index(): #用來回應網站首頁連線的函式
    return "Hello Flask" #回傳網站首頁內容

@app.route("/test") #代表我們要處理的網站路徑
def test():
    return "this is test"

if __name__=="__main__"
#啟動網站伺服器,可透過port指定埠號
    app.run(port=3000)