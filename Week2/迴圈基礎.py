# for c in "Hello":
#     print(c)

# for x in [2,2,3,4,5]:
#     print(x)

# for y in range(3): #=[0,1,2]
#     print(y) # 0 1 2
# #for迴圈
# sum=0
# for a in range(1,11):
#     sum = sum + a
# print(sum)


# n=0
# for e in [0,1,2,3]:
#     if e%2==0:
#         continue
#     print(e)
#     n+=1
# print(n) #1,3 #2

# message = "Hello, World!"
# for char in message:
#     print(char)

# person = {"name":"Alice","age":30,"city":"New York"}
# for key,value in person.items():
#     print(key,":",value)

#整合範例:找出整數平方根
n=input("12")
n=int(n)
for i in range(n):#i 0 ~ n-1
    if i*i==n:
        print("整數平方根", i)
        break
else:
    print("沒有整數平方根") #5

