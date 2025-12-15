#what is function?
#code ke shajiye-guchiye ekta block er majhe lekhar prokriya ke function bole.

#Use case of function:
#1. code reusability
#2.Modular programming: ek-ekta function ke ek-ekta modul bola hye thake. eivabe ek-ekta function ba ek-ekta modul akare lekhar ei habit ta ke bola hye thake modular programming.
#3.Event Handling
#4.Testing, validation

#||Defining_&_calling_a_function:||
#function ke likhar jonno "def" name er ekta keyword ache ja lekha lage. Ar ei "def" diye bujhanu hoy define kra.
#example:
"""
def addTwo():
    a = 10
    b = 20
    c = a + b
    print(c)

addTwo()  #[eivabe ekta function ke print dite hoy. just function er name dhore call krlei heb]
"""

#||Function with parameters:||
#Function_with_parameters:
"""
def addTwo(x, y):    #[eikhane "(x, y)" eita parameter]
    z = x + y
    print(z)
addTwo(10, 30)     #[eikhane "(x=10, y=30)" parameter er value pass kra holo]
addTwo(10, 300)
addTwo(100, 30)
"""

"""
def addTwo (a, b, c, d):
    e = a + b + c + d
    print("four number addition is here:", e)
addTwo(10, 20, 30, 40)       #[eivabe coding ke function with parameters bole]
"""

#Defaults/Optional_parameters:
"""
def addTwo(a, b, c=0, d=0):    #[eikhane duita value aage theke asign kra ache]
    e = a + b + c + d
    print(e)
addTwo(10, 20, 30, 40)     #[eikhane first er dike default value assign kra ache 'c'&'d' jdi parameters e value pass kra hy tahole oi value ta niye kaj krbe]
addTwo(10, 20, 30)
addTwo(10, 20)
"""

#Rest_parametera / Variable-Length_arguments(in python eita called kra hoy):
"""
def addTwo(*a):    #[jokhn onek gula parameters print kra lagbe tokhn amra eivabe likhbo]
    print(a)
    #print(list(a)) #[jodi amra output ta tuple akare na deke list akare dekhte cai tokhon eivabe print krte hbe]
addTwo(1)          #[eikhane joto gula value pathay na keno shob gula value receive kre tuple akare show krbe]
addTwo(1,2)
addTwo(1,2,3)
addTwo(1,2,3,4)
addTwo(1,2,3,4,5)
addTwo(1,2,3,4,5,6)
"""

#Keyword parameters:
"""
def nazim(**a):    #[eikhane ei function name "**a" diye "nazim function" e assign kra "key" ar "value" gula aksathe dhorte pereche]
    print(a)       #[eikhane ei "key" ar "value" gula ke receive kre then dictionary akare show kre]

nazim(fName = "Mmd Nazim", hFrom = "AIUB", p = "CSE")
"""

#Function_return:
#remember this line "ekta function jaha return kre taha ghune ebong mane uhar shoman hye jay"
"""
def addTwo():
  a = 10
  b = 20
  c = a + b
  return c   #[ami jei value e return kri na keno oi function ta oi typer hye jabe ...Example: ami ekhn return jdi kri integer taholr oi functon tao ekta integer value]
result = addTwo()  #=30=int
print(result + 10)
"""

#Function_return_nothing:
"""
def addTwo():
  a = 10
  b = 20
  c = a + b
  print(c)

addTwo()   #[eikhane kono "return" keyword ta e nai tai eikhane kono valuer type return krbe na]
"""

#Function_return_multiple_values:
"""
def addTwo():
  return 25, "Nazim", "Dhaka", True  #[ekta function e jdi multiple  ]

age,name,city,isBangladeshi =  addTwo()   #[ekta function e jdi multiple boishishtho thake tokhon take mutiple name dhara likhte hoy]

print(age)
"""

#Short_hand_function/Inline_function/Lamda_function:
"""
#Normal_function:
def addTwo(x, y):
  z = x + y
  return z

print(addTwo(10, 20))

#Convert_to_the_lambda_function:
# 1.lambda auto return kre
# 2.lambda function er kono name nei but ekjon obhivabok ache like "demo"
demo = lambda x, y : x + y
print(demo(10,20))    #[lambda te return kaje lage na]
"""


#Function_scope: Function scope are 2 types. 1.Local function scope 2.Global function scope
"""
#Function_scope(Local): jodi kono function er bitore variable declar kra hoy ebong oi variable onno kothao use kra jay na take local function scope bole.
def myFunc1():
    x = 10
    y = 20
    print(x + y)

def myFunc2():
  x = 100
  y = 200
  print(x + y)

myFunc1()
myFunc2()

#Function_scope(Global): Ekta variable declar krar por jdi oi variable take onno jekono fuction access krte pare tokhon take global function scope bole.
z = 300
def myFunc1():
  x = 10
  y = 20
  print(x + y + z)


def myFunc2():
  x = 100
  y = 200
  print(x + y + z)

myFunc1()
myFunc2()
"""
#NOTE_That:
#function er kono specific return type nai.
#function er return type ta dynamic and it can be any valid python object.
