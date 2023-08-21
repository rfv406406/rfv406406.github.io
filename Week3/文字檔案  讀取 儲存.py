#儲存檔案
# file=open("data.txt", mode="w", encoding="utf-8")
# file.write("Hello\nWorld")
# file.close()

# with open("data.txt", mode="w", encoding="utf=8") as file:
#     file.write("測試中文\n好棒棒")

# with open("data.txt", mode="w", encoding="utf=8") as file:
#     file.write("5\n3")

#讀取檔案

# with open("data.txt", mode="r", encoding="utf-8") as file:
#     data=file.read()
# print(data)
# sum=0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     for line in file:
#         sum+=int(line)
# print(sum)

#使用JSON格式讀取複寫檔案

import json

with open("config.json", mode="r") as file:
    data=json.load(file)
print(data)  #字典資料
print("name:", data["name"])
print("name", data["version"])

data["name"]="Bndy" #資料修改

with open("config.json", mode="w") as file:  #複寫資料
    json.dump(data, file)


