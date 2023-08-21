from flask import Flask #載入Flask
from flask import request

app=Flask(__name__) #建立Application物件

#建立路徑/對應的處理函式
@app.route("/") #函式的裝飾(decorator):已函式為基礎，提供附加功能。
def index(): #用來回應路徑/的函式
    # print("請求方法", request.method)
    # print("通訊協定". request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址", request.url)

    # print("瀏覽器和作業系統", request.header.get("user-agent"))
    # print("語言偏好", request.header.get("accept-language"))
    # print("引薦網址", request.header.get("referrer"))
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Flask"
    else:
        return "您好，歡迎光聯"

    return "Hello Flask"




#啟動網站伺服器,可透過port指定埠號
    app.run(port=3000)