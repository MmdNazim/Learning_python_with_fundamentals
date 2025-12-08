                                         #||Numeric_data_type:||
#Int_type_data:
"""
a = 10
b = 5
c = a + b
print(c)
"""

#Float_type_data:
"""
q = 10
w = 3
e = q/w

print(e)
"""

#Complex_type_data:

                                        #||String_data_type:||
#Single_quote_string:
"""
name = 'Nazim is a "gentalboy"'   #NOTE:[Jodi kono shmy double quotes er drkar hoy tokho full string ke wrap up krar jonno single qoutes lage.]
print(name)
"""

#Double_quote_string:
"""
name = "Nazim's creation 'World'"
print(name)
"""

#Triple_quote_string: Triple quotes abar 2 types: 1.Triple single quote 2.Triple double quote
#Triple quoter kaj hocche multiple text jokhon likhbo string declarationer time e tokhon oi text gula ke single line na likhe multiple line likhar jonno ei Triple quotes use kre.

#Triple Single quotes:
"""
aboutMe ='''
Hello, Mia Md Nazim. Now you are a student of python course.
you have to focus on your python skill which is very important to you,
for build your amazing career.
'''
print(aboutMe)
"""

#Triple double quotes:
helloMe ="""
Hello Mia Md Nazim. Now you are a student of python course.
you have to focus on your python skill which is very important to you
for build your amazing career.
"""
print(helloMe)


                                      #||Sequence_data_type:||
#Sequence data type hocche emn ekta data type jeikhane onek gula data store kra jabe eksathe.
#Different types of kinds of sequence data types are available: 1.list [#list ke eivabe square brackets er majhe declar kra hoy]
#2.Tuple (tuple ke eivabe first brackets er majhe declar kra hoy. eitao ekta ordered data type.)
#3.Range type

#List_type: list data type ke abar ordered data type bola hoy.
"""
fruits = ["apple", "Banana", "Orange", "Tangerine"]
print(fruits)
print(fruits[2])   #eivabe index dhore data fetch kre.
"""

#Tuple_type:
"""
fruits1 = ("apple", "Banana", "Orange", "Tangerine")
print(fruits1)
print(fruits1[3])
"""

#Range_type: Eitao ekta ordered data type bola hoy. Indexing kre eikhan thekeo data fetch kra jabe.
"""
numbers = range(1, 10)
print(numbers)
print(*numbers)   #Eikhane '*' dhara shob gula data show kra jay.
"""

                                         #||Mapping_data_type:||
#Mapping data types er majhe pawa jay: 1.Dictionary types
#Eikhaneo sequence types er datar moto onekgula data store kra jay.
#But ei Mapping ar Sequence data type duitar majhe difference hoilo sequence types er data ordered way te thake ar mapping er data unordered way te thake.

#Dictionary_type:
"""
person = {
    'name' : 'Nazim',
    'age' : 25,
    'gender' : 'Male',
    'City' : 'Comilla'

   #NOTE:
    #'name' : 'Nazim'
    #key[key er value always string hbe.] : value[eikhaner value ta any typer hoite pare.] #[eikhane ekta key ar ekta value pair hishabe thake.]
}
print(person)
print(person['name'])
"""

                                         #||Set_data_type:||
#set holo two types: 1.sets 2.Frozensets
#set holo ekta unordered data type.

#Set_type: sets declar krar time e "{}" second bracket use kra hoy. Sets e store kra duplicate value gula ekbar e read kre.
"""
numbers = {1,2,3,4,5}
letters = {'a', 'b', 'c'}
print(numbers)
print(letters)
"""

#Frozenset_type: Frozenset ekta unordered data type.
"""
letters = frozenset(['a', 'b', 'c'])
print(letters)
"""

                                         #||Boolean_data_type:||
#Boolean data type duita value return kre "True" or "False".
"""
isBangladeshi = True
print(isBangladeshi)
"""
"""
isLogin = False
if isLogin==True:
  print("Account Link")
else:
  print("Login Link")
"""



                                         #||None_data_type:||
"""
myMoneyBag = None
print(myMoneyBag)
"""

"""
data = None
if data == None:
    print("Loading...........") 
else:
    print("Load web page view")
"""

                                      #||Mutable_&_Immutable_data_type:||
#Mutable_types: ei data types er bitore pore lists, dictionaries, set
#immutable_types: int, float, str, tuple, frozenset.

                                         #||Type_conversion||
#Type conversion abar 2 dhoroner 1.Explicit type conversion 2.Implicit type conversion

#Implicit_type_conversion: Ei method e python ekta datatype theke arekta datatype e convert kre automatically.
a = 10
b = 3
c = a/b
print(c)
print(type(c))

#Explicit_type_conversion: Eikhane user variable er datatype ke tar required datatype nite kichu method use kre convert krte pare.
#Method gulu holo: int(), float(), str()
a = "123"
int_value = int(a)
float_value = float(a)
str_value = str(a)

print(int_value)
print(float_value)
print(str_value)

#Handling_conversion_error:
try:
    name = "Nazim"
    con_int = int(name)
    print(con_int)
except Exception as e: #(eita ekta variable)
    print(e)





















