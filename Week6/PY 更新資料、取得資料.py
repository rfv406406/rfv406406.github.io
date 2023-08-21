import mysql.connector
#連線到資料庫
con=mysql.connector.connect(
    user="root",
    password="rfv406406",
    host="127.0.0.1",
    database="mysql"
)
print("Success")  #連線成功

#建立Cursor物件，用來對SQL下指令
cursor=con.cursor()
#更新資料，刪除(語法更改)
productName="美式咖啡"
productId=1
cursor.execute("UPDATE product SET name=%s WHERE id=%s", (productName, productId))
con.commit() #執行
#取得資料
cursor.execute("SELECT * FROM product WHERE id=2")
data=cursor.fetchone()
print(data)
print(data[0], data[1])
#取得多筆資料
cursor.execute("SELECT * FROM product")
data=cursor.fetchall()
print(data)
#逐一取得
for row in data:
    print(row)
    print(row[0],row[1])
con.close() #關閉資料庫