#程式包裝
# def calculate(max):
#     sum=0
#     for x in range(1,max+1):
#         sum=sum+x
#     print(sum)

# calculate(10)  #55
# calculate(20)  #210


def divide(n1,n2):
    print(n1/n2)
divide(2,4) #0.5
divide(n2=2,n1=4) #2

# def avg(*ns):  #*不定參數 (多參數) 

# avg(3,4)
# avg(3,5,10)
# avg(1,4,-1,-8)


def avg(*ns):  #*不定參數 (多參數)
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))     

avg(3,4) #3.5
avg(3,5,10) #6.0
avg(1,4,-1,-8) #-1.0