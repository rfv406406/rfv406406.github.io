#初始化Flask伺服器
from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
import json

app = Flask(
    __name__,
    static_folder= "templates",
    static_url_path= "/",
)
app.secret_key = "any string but secret"

import mysql.connector

con=mysql.connector.connect(
    user = "root",
    password = "rfv406406",
    host = "127.0.0.1",
    database = "website")

# 建立 Cursor 对象，用来执行 SQL 指令
# cursor = con.cursor()
# 確保導入json模塊

def abc():
    # 建立數據庫連接（使用實際的數據庫連接細節替換這些內容）

    # 建立游標
    cursor = con.cursor(dictionary=True)

    # 執行查詢
    cursor.execute("SELECT id, name, username FROM member")

    # 讀取一行數據
    data = cursor.fetchone()
    print(data)

    # 創建包含數據的字典
    name_dict = {
        "data": data
    }

    # 將字典轉換為JSON
    json_name_dict = json.dumps(name_dict)
    print(json_name_dict)

    # 關閉游標和數據庫連接
    cursor.close()
    con.close()  # 確保在這一行之後沒有多餘的字符

# 調用函數
abc()