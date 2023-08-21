def func(*data):
    count = {}
    middle_names = []  

    for name in data:
        middle_name = name[1]  
        middle_names.append(middle_name)  
        count[middle_name] = count.get(middle_name, 0) + 1 

    for second_name in middle_names:
        if count[second_name] == 1: 
            print(name) 
            return

    print("沒有")  


func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

 
