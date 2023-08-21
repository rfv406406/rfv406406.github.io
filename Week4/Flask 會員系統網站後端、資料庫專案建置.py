#初始化資料庫連線
import pymongo
client=pymongo.MongoClient("連線網址")
db=client.member_system

#初始化Flask伺服器
from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/",
)
app.secret_key="any string but secret"
app.run(port=3000)