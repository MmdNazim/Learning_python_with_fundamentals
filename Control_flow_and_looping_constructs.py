#Control_flow:
                                            #||If_Statement:||
#NOTE:[If statement er kaj holo ekta statement niye kaj kora. jodi oi statement condition fulfill kre then eita result show kre otherwise kono statement e show kre na.]
"""
age = 1
if age >= 18:
    print("you are adult")
"""

#||Else_Statement:||
"""
isLogin = False
if isLogin == True:
    print("Logged in")
else:
    print("Not logged In")

age = 18
if age >= 18:     #[Eikahne "age>=18" eita condition ar ":" coloner mane hoilo condition ta sesh kra.]
    print("you are adult")
else:
    print("you aren't adult")
"""

                                             #||Else If(elif)_Statement:||
#Jokhon onek gulu condition hbe tokhn amra else if statement use krbo.

"""
marks = 9
if marks <= 100 and marks >= 80:
    print("A+")
elif marks <= 80 and marks >= 70:
    print("A")
elif marks <= 70 and marks >=60:
    print("A-")
elif marks <= 60 and marks >=50:
    print("B")
elif marks <= 50 and marks >=40:
    print("C")
elif marks <= 40 and marks >=33:
    print("D")
else:
    print("F")
"""

"""
# Nested If else statement:
age = input("enter your age: ")
age = int(age)
has_permission = False

if age >=  18:
    if has_permission == True:
        print("you can enter the club")
    else:
        print("you need permission to enter the club")
else:
    print("you are not allow to enter the club")
"""

                                              #||For_Loop|| 
#List_er_upor_for_loop_apply/for loop iterating over a list:
"""
menu = ['Home', 'About', 'Courses', 'Community', 'Information']
for item in menu:   #[1.Eikhane "item" holo list er majhe joto gula input dewa ache indiviual tara ek ekta "item". 2.Ar eikhane "in" dhara bujhanu hoise je kar theke item gula ber kre anbo sheita. 3.And amra menu theke "item" ber kre anbo tai "in" er pore "menu" variable ta add kra hoise.]
    print(item)     #[Eikhane per "item" ber krbo tai "item" ta print dewa hoise.]
"""
"""
city = ['Dhaka', 'Chittagong', 'Comilla', 'Barisal']
for item in city:
    print(item)
"""

"""
list = ["a", "b", "c", "d"]
for eachItem in list:
    print(eachItem)
"""    

#Word_upor_For_loop_apply/For loop iterating over a string:
"""
name = "Python"
for item in name:
    print(item )
"""

"""
letter = "hello"
for Item in letter:
    print(Item)
"""

#For loop using range() function:
"""
for item in range(100):
    print(item)
"""

#For loop iterating over a Dictionary:
"""
eaxmResult = {'phy':90, 'math':89, 'bangla':70}
for subject,marks in eaxmResult.items():
    print(subject)
    print(marks)
    print("Subject:"+subject+"Marks:"+str(marks))
    print("{}:{}".format(subject,marks))      #[NOTE: this is called string formatting way] 
"""

"""
person = {
    "name" : "jahan",
    "age" : 25,
    "country" : "Bangladesh"
}
#person.item()    #[NOTE: eikhane first of all "person" variable ta dictionary theke list convert kra holo ei process e]

for key, value in person.items():
    print(value)
"""

#For loop iterating over a set:
"""
unique_numbers = {1, 2, 3, 4, 5}
for eachItem in unique_numbers:
    print(eachItem)
"""    

                                           #||Break_statement:||
"""
country_list = ['Bangladesh', 'Saudi-Arabia', 'Pakistan', 'Norway', 'USA', 'Denmark', 'Sweden', 'Japan', 'China']
for item in country_list:
    if item == 'USA':      #[Eikhane "If statement" use kre list er specific item declar kre tar aag porjhonto list er item access kra jay eivabe.]
        break              #[Specific jaygay loop ke thamanur jonno "break" use kra hoy.]
    print(item)
"""

"""
for num in range(10):
    if num == 5:
        break
    print(num)
"""    

                                          #||Continue_statement:||
"""
name_list = ['Shawon', 'Farhan', 'Arnob', 'Shakil', 'Mahin', 'Imran']
for item in name_list:
    if item == 'Arnob':
        continue      #[Eikahne "continue" mane hocche kono kichu 'SKIP' kra. Eikhane "Arnob" ke skip kre baki shob gula item ke show kra hyeche.]
    print(item)
"""

"""
for num in range(10):
    if num == 5:
        continue
    print(num)
"""
                                         #||While_loop:||
#For_loop eitar alternate hishabe while loop use krte pari. While_loop automatically index number count krte pare na.

#while loop iterating over a list:
"""
city = ['Dhaka', 'Chittagong', 'Barisal', 'Comilla', 'Khulna']
index = 0  #[Jehoto while loop index number count krte pare na tai eikahne index number koto theke start hbe sheita initialize kra hyeche.]
while index < len(city):  #[Eikhane "index" kota theke start hbe ta bole dewa ache, oikhan theke start hye "city" list er length sesh howar sathe sathe ei while loop end hbe.]
    print(index)
    index = index + 1      #[Eikhane index number koto kre barbe ta bole dewa ache.]
"""

"""
fruits = ['apple', 'banana', 'cherry']
index = 0
while index < len(fruits):
    #print(index)
    print(fruits[index])
    index = index + 1
"""

#while loop iterating over a string:
"""
word = "hello"
index = 0
while index < len(word) :
    print(word[index])
    index = index + 1
"""

#While_loop_use_kre_100_times_name_print:
"""
index = 0
while index < 100:
    print("Nazim")
    index = index +1
 """

#While_loop_use_kre_(1-10)_times_print:
"""
index = 0
while index < 10:
    print(index)
    index = index +1
"""

#While_loop_use_kre_"2"kre_number_barle_koto_hoy_tar_print:
"""
index = 0
while index < 10:
    print(index)
    index = index +2
"""

#While_loop_use_kre_"3"kre_number_barle_koto_hoy_tar_print:
"""
index = 0
while index < 10:
    print(index)
    index = index +3
"""

"""
index = 0
end = 10

while index < end :
    print(index)
    index = index + 1
"""

#while loop iterating over a list:
"""
country_list = ['Bangladesh', 'Saudi-Arabia', 'Pakistan', 'Norway', 'USA', 'Denmark', 'Sweden', 'Japan', 'China']
index = 0
while index < len(country_list):
    print(country_list[index])   #[Eikhane ei process er majhe "country_list" ei list er majhe jhoto item ache shob gula show kra jabe.]
    index = index + 1
"""

#Using break statement with While_loop:
"""
country_list = ['Bangladesh', 'Saudi-Arabia', 'Pakistan', 'Norway', 'USA', 'Denmark', 'Sweden', 'Japan', 'China']
index = 0
while index < len(country_list):
    if country_list[index] == 'Norway':
        break
    print(country_list[index])
    index = index + 1
"""

"""
index = 0
end = 10

while index < end :

    if index == 5 :
        break
    print(index)
    index = index + 1
"""

#Using continue statement with While_loop:
"""
country_list = ['Bangladesh', 'Saudi-Arabia', 'Pakistan', 'Norway', 'USA', 'Denmark', 'Sweden', 'Japan', 'China']
index = 0
while index < len(country_list):
    if country_list[index] == 'USA':
        index = index + 1   #[NOTE: Increment index is  use here to avoid an infinite loop]
        continue
    print(country_list[index])
    index = index + 1
"""

"""
index = 0
end = 10

while index < end :

    if index == 5 :
        index = index + 1    #[NOTE: Increment index is  use here to avoid an infinite loop]
        continue
    print(index)
    index = index + 1
"""

#while loop iterating over a dictionary:
"""
examResult = {"Bang":90, "eng":92, "math":95}
keys = list(examResult.keys())

index = 0
while index < len(keys) :
    #print(keys[index])      #[NOTE: eikhane dictionary er key gula print kra hyeche]
    eachKey = keys[index]
    #print(examResult[eachKey])     #[NOTE: eikhane dictionary er value gula print kra hyeche]
    outPut = eachKey +": " + str(examResult[eachKey])     #[NOTE: eikhane dictionary er key & value duitai print kra hyeche]
    print(outPut)
    index = index + 1
"""

#while loop iterating over a dictionary:
"""
my_set = {1,2,3,4,5}
my_list = list(my_set)

index = 0
while index < len(my_list) :
    print(my_list[index])
    index = index + 1
"""









