from flask import Flask #載入Flask
from flask import request
#建立Application物件
app=Flask(__name__,
          static_folder="static",
          static_url_path="/"
          ) 

#建立路徑 /getSum 對應處理函式
#利用要求字串(Query String)提供彈性: /getSum?max=最大數字
@app.route("/getSum")
def getSum(): #1+2+3..+max
    maxNumber=request.args.get("max", 100)
    maxNumber=int(maxNumber)
    result = 0
    for n in range(1,maxNumber+1):
        result+=n
    return "結果:"+str(result)

#啟動網站伺服器,可透過port指定埠號
    app.run(port=3000)