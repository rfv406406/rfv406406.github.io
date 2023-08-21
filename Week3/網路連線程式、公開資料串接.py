# import ssl
# import urllib.request as request

# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")#取得台灣大學網站原始碼(HTML、CSS)
# print(data)

#串接、擷取公開資料
import ssl #使用SSL module把證書驗證改成不需要驗證
ssl._create_default_https_context = ssl._create_unverified_context 

import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式
#將公司名稱列表出來
clist=data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")   #\n 換行符號
        
print(company["公司名稱"])