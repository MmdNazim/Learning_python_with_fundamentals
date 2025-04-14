"""
print("hello python")
print("hello python 2")
print("hello python 3")
print("hello python 4")
"""

"""
name =  "Nazim"
age = 25
edu = "Bsc in CSE"
print(name, age, edu)
"""
#Addition:
# a = 20
# b = 10
# c = a +b
# print(c)

#Substraction:
# a = 20
# b = 10
# sub = a-b
# print("Here is answer:",sub)

#Multiply:
# a = 20
# b = 10
# c = a*b
# print("Result is:",c)

#Divide:
# a = 20
# b = 10
# c =  a/b
# print("result is:", c)

#Variables:
# name = "Nazim Ahmed"
# print(name)

                               #||Data_Types||

#Numeric Data Types
# age = 25 #int data type
# print(age)

# marks = 85.5  #float data type
# print(marks)

# complex_number = 10+20j  #complex data type
# print(complex_number)

#String Data Types
# name = "Mia Md Nazim"
# print(name)

#Sequence Data Types:
"""
#Sequence Data Types:(List data types)
city = ["Dhaka", "Rajshahi", "Khulna"]
city = ["dhaka", 20, 85.5 ]  #list er majhe mixed value rakha jay.
city = ["Dhaka", "Rajshahi", "Khulna", "Dhaka", "Rajshahi", "Khulna" ]  #list er majhe dublicate value rakha jay.
print(city)
letters = ["A", "B", "C", "D"]
print(letters[3])  #List er majhe index dhore dhore value print kra jay.
"""

"""
#Sequence Data Types:(Tuple data types)
letter = ("A", "B", "C", "D", "E")
letter2 = ("A", "B", "C", 20, 20.22)  #tuple er majhe mixed value rakha jay.
letter3 = ("A", "B", "C", "D", "E", "A", "B", "C", 20, 20.22)  #tuple er majhe dublicate value rakha jay.
print(letter3)
"""

"""
#Sequence Data Types:(Range data types)
numbers = range(1, 10)     #[eikhane "1" hocche starting pont ar "10" tar agg porjhonto oi range er value show krbe.]
numbers2 = range(1,10,2)   #[eikhane "1" hocche starting pont ar "10" hocche range er stop point and "2" hocche koto kre barbe tar sequence.]
numbers3 = range(10)       #[eikhane ranger starting point declar nei, but by default python range 0 theke start kre.]
print(*numbers2)           #[jodi pura range dekhte cai tahole variabler age "*" dite hbe.]
print(*numbers3)
"""

"""
#Boolean Data Type:
isBangladeshi = True
print(isBangladeshi)
isBangladeshi = False
print(isBangladeshi)
"""

"""
#None Data Types:
taka = None
print(taka)
"""

"""
#Mapping Data Type/Dictionary Data Type:
person = {
    'first_name' : 'Mmd',
    'last_name' : 'Nazim',
    'age' : 25,
    'isBangladeshi' : True
}
#print(person)
print(person['age'])  #[etto gula properties er majhe specific ekta property ber krte pari eivabe.]
"""

"""
#Set Data Types: (1.Set-mutable)
unique_numbers = {1, 2, 3, 4}
unique_numbers2 = {1, 2, 3, 3, 4, 4, 5, 6, 6}  #[eikhane set duplicate value gula ke baad diye only unique value return kre.]
print(unique_numbers2)
#print(unique_numbers[1])  #[eikhane kono idexing kaj krbe na eigula holo unordered typer data.]
"""

"""
#Set Data Types: (2.Frozenset-immutable)
unique_numbers = frozenset([1, 2, 3, 4])
unique_numbers2 = frozenset([1, 2, 2,  3, 3,  4, 5])  #[eikhane set duplicate value gula ke baad diye only unique value return kre.]
print(unique_numbers2)
#print(unique_numbers[0])  #[eikhane kono idexing kaj krbe na eigula holo unordered typer data.]
"""











