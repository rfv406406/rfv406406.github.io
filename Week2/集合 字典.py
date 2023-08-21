#集合
S1={1,2,3}
print(10 in S1)  #False
print(10 not in S1)  #True

S1={3,4,5}
S2={4,5,6,7}
S3=S1&S2 #交集
S4=S1|S2 #聯集
print(S3) #{4,5}
print(S4) #{3,4,5,6,7}

S5=S1-S2 #差集
print(S5) #{3}

S6=S1^S2 #反交集
print(S6) #{3, 6, 7}

s=set("Hello")
print(s)
print("A" in s)

#字典  #鍵值對

dic={"apple":"蘋果","bug":"蟲"}
print(dic["apple"]) #蘋果
dic["apple"]="小蘋果"
print(dic["apple"]) #小蘋果
print("test" in dic)

dic={x:x*2 for x in [3,4,5]}
print(dic)



