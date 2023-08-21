import mysql.connector
#連線到資料庫
con=mysql.connector.connect(
    user="root",
    password="rfv406406",
    host="localhost",
    database="mysql"
)
print("Success")  #連線成功

#建立Cursor物件，用來對SQL下指令
productId=6
productName="奶綠"
cursor=con.cursor()
#執行執行SQL指令，帶入資料變數。如果只有單一資料，後面,要保留。
cursor.execute("INSERT INTO product(id, name) VALUES(%s, %s)", (productId, productName)) 
con.commit() #執行
con.close() #關閉資料庫
