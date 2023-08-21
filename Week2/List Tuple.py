#List 

grades=[12,60,15,70,90]
grades=grades+[12,33]
print(grades) #[12,60,15,70,90,12,33]

length=len(grades)
print(length) #7

data=[[3,4,5],[6,7,8]]
print(data[0]) #[3,4,5]
print(data[0][0]) #3
data[0][0:2]=[5,5,5]
print(data)

#Tuple

data=(3,4,5)
# data[0]=5  #錯誤

data=data+(1,2)
print(data)