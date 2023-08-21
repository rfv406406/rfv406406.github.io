#網址與資料夾對應關係


from flask import Flask #載入Flask


#建立Application物件,可以設定靜態網站路徑

app=Flask(
    __name__,
    static_folder="static", # 靜態網址對應名稱
    static_folder_url_path="/static" #靜態檔案對應的網址路徑
    )

# 所有在static資料夾底下的檔案,都對應到網址路徑 /static/檔案名稱

#建立路徑/對應的處理函式
@app.route("/") #函式的裝飾(decorator):已函式為基礎，提供附加功能。
def index(): #用來回應路徑/的函式
    return "Hello Flask" #回傳網站首頁內容

@app.route("/data") #建立路徑/data剁硬地處理函式
def handleData():
    return "My Data"

# 動態路由:建立路由/user/使用者名稱 對應的處理函式
@app.route("/user/<username>")
def handleUser(username):
    if username == "康康":
        return "你好"+username
    else:
        return "Hello" + username

#啟動網站伺服器,可透過port指定埠號
    app.run(port=3000)