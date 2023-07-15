1.
# 18 years old,college student,legal age,will vote 選以上字串定義為年齡>17歲。
def find_and_print(messages):
    for key in messages:
        if "18 years old" in messages[key] or "college student" in messages[key] or "legal age" in messages[key] or "will vote" in messages[key]:
            print(key)

find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})

2.
def calculate_sum_of_bonus(data):
# above average獎金為本薪*0.1，average為本薪*0.05，below average為本薪*0.025
    bonuses = 0

    for i in range(len(data["employees"])):
        salary = data["employees"][i]["salary"]
        performance = data["employees"][i]["performance"]
        bonus = 0

        if isinstance(salary, str):
            if "USD" in salary:
                salary = float(salary.replace("USD", "")) * 30
            else:
                salary = float(salary.replace(",", ""))

        if performance == "above average":
            bonus = salary * 0.1
        elif performance == "average":
            bonus = salary * 0.05
        elif performance == "below average":
            bonus = salary * 0.025

        bonuses = bonuses + bonus

    print("Total:", int(bonuses))

calculate_sum_of_bonus({
"employees":[
{
"name":"John",
"salary":"1000USD",
"performance":"above average",
"role":"Engineer"
},
{
"name":"Bob",
"salary":60000,
"performance":"average",
"role":"CEO"
},
{
"name":"Jenny",
"salary":"50,000",
"performance":"below average",
"role":"Sales"
}
]
}) # call calculate_sum_of_bonus function

3.
def func(*data):
    
    names = []
    
    for name in data:
        middlename = list(name)
        names.append(middlename[1])

    hashTable = {}
    for item in names:
        if item in hashTable:
            hashTable[item] += 1
        else:
            hashTable[item] = 1

    nomatch = True
    for middleName, count in hashTable.items():
        if count == 1:
            print(wholenames(data, middleName))
            nomatch = False

    if nomatch:
        print("沒有")

def wholenames(names, middleName):   
    for name in names:
        middlename = list(name)
        if middlename[1] == middleName:
            return name
        
func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

4.
def get_number(index):
    x = 4
    y = -1
    result = 0

    remainder = index % 2

    if remainder == 0:
        result = (index // 2) * (x + y)
    elif remainder > 0:
        result = (index + 1) // 2 * (x + y) + 1

    print(result)

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15