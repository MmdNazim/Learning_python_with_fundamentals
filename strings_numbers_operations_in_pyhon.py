import math
                                           #||String||
#Different types of strings:
#1.Single quote string
str1 = 'hello nazim'
#2.Double quote string
str2 = "hello double nazim"
#3.Triple single quote string
str3 = '''
hello nazim ki koroch eikhane bhala asos ni kita krmu koch na, hudai boissha boissha 
likhtasi kam kaj nai jsut practice arki.matha noshto proramming bojjo :3
'''
#4.Triple double quote string
str4 = """
hello nazim ki koroch eikhane bhala asos ni kita krmu koch na, hudai boissha boissha 
likhtasi kam kaj nai jsut practice arki.matha noshto proramming bojjo :3
"""

#String is immutable #(immutable means: she nije nije change hoy na borong dhongsho hye oi ek e jaigay noton kre create hoy.)
"""
country = "Bangladesh"
country = "Bangladesh2.0"
country = "Bangladesh3.0"
country = "Bangladesh4.0"
country = "Bangladesh5.0"
country = "Bangladesh6.0"
print(country)
"""

#String_indexing:
#Positive Indexing: left to right index counting ke positive indexing bole.   #[0,1,2,3,4,5,6,7,8,9]
#Negative indexing: right to left index counting ke negative indexing bole. Negative indexing start hoy "-1" theke.
#[-1,-2,-3,-5,-6,-7,-8,-9,-10]
"""
myCountry = "Bangladesh"
print(myCountry[1])
"""

#String_slicing:
"""
country = "Bangladesh"
print(country[0 : 6])    #[Eikhane '0' index theke start '6' index er ager index porjhonto show krbe.]
print(country[:6])       #[by default eikhane '0' index theke start hbe.]
print(country[3:7])
print(country[3:])       #[by default eikhane last index porjhonto show krbe.]
"""

#String_concatenation:
"""
firstName = "Mia Mohammad"
lastName = "Nazim"
fullName = firstName + " " + lastName

print(fullName)
"""

#String_repetition:
"""
firstName = "Mmd"
lastName = "Nazim"
fullName = firstName + " " + lastName
print(fullName)

fullName1o = fullName * 10    #[Ei process ke string repetition bole.]
print(fullName1o)
"""

#String_formation:
#amra '%' sign use kre string formation er kaj krte pari.
#First_way_of_formation: Ei process ke abar place holder process bola hye thake.
"""
name = "Hamid"
age = 35
fullName = "My name is= %s and age is= %d" %(name, age)   #[Eikhane 's' dhara string & 'd' dhara decimal number boshbe. Ar eikhane bracket er name ar age dhara 's' ar 'd' ke replace kra hyeche.]
print(fullName)
"""

#second_way_of_formation: Eikhane 'format()' method use kra hoy.
"""
fName = "Hamid"
lName = "Khan"
age1 = 35
fullName1 = "My name is= {} {} and age is= {}" .format(fName, lName, age1)
print(fullName1)
"""

#Third_way_of_formation: Amra ei process ta real life project e use krbo.
"""
fName = "Hamid"
lName = "Khan"
age1 = 35
fullLine = f"My name is {fName} {lName} and age is {age}"
print(fullLine)
"""

#String_methods:
#1.Uppercase_method:
"""
country = "Bangladesh is my country"
str = country.upper()
print(str)
"""

#2.Lowercase_method:
"""
country = "Bangladesh is my country"
str1 = country.lower()
print(str1)
"""

#3.Capitalcase_method:
"""
country = "bangladesh is my country"
str2 = country.capitalize()
print(str2)
"""

#4.Titlecase_method:
"""
country = "bangladesh is my country"
str3= country.title()
print(str3)
"""

#String_replace_method:
"""
country = "bangladesh is homeland"
result = country.replace('homeland', 'motherland')  #[eikhane "replace('kake shorabo oita', 'jake diye shorabo eita eikhane likhbo')"]
print(result)
"""

#String_split_method:
"""
country = "bangladesh is my homeland"
result = country.split()
print(result)
"""

#String_white_space:
"""
country = "      bangladesh is my homeland     "
result = country.strip()       #[Ei method er dhara both side er white space shoranu jai.]
result1 = country.rstrip()     #[Ei method e right side er white space shoranu jabe.]
result2 = country.lstrip()     #[Ei method e left side er white space shoranu jabe.]
print(result)
print(result1)
print(result2)
"""

#string_insides: Eikhan string er majhe kono kichu search kre ber krte pari.
"""
country = "hello mmd nazim"
result = country.startswith("hellooo")
#[Eikhane "startsWith()" ei method er bhitore declar kra string er sathe jdi variable declar kra sentence tar starting point er sathe mil pai tahole ta boolean value 'true' return kre ar jdi na mile tahole 'false' return kre.]
result1 = country.endswith("nazim")
#[Eikhane "endswith()" ei method er bhitore declar kra string er sathe jdi variable declar kra sentence tar ending point er sathe mil pai tahole ta boolean value 'true' return kre ar jdi na mile tahole 'false' return kre.]
result2 = country.find("mmd")
#[Eikhane "find()" ei method dhara declar kra sentence e oi word ache kina ta khujhe ber kra jay.]
print(result)
print(result1)
print(result2)

result3 = country.count("m")  #[Ei 'count("m")' method dhara koto bar ei sentence ba word ta oikhane ache tar information jana jay.]
print(result3)
result4 = country.isdigit()   #[ei "isdigit()" method dhara bujha jay je declar kra sentence digit ache kina ta ber kra jay.]
print(result4)
"""
                                         #||Operator:||
#Operator_precedence: Eikhane python ekta sequence wise kaj kre.
#Different types of operator precedence ache:
#[** (exponentiation)]
#[+x(u-nary plus), -y(u-nary minus)]
#[*, +, %]
#[+, -]
#[<< >> (bit wise operator)]
#[&(and operator)]
#[|(or operator)]
#[==(equal equal operator), !=(not  qual operator)]
#[<(less then operator), >(greater then operator), =<, =>, is, is not, in, not in]
#[logical operator(AND, OR, NOT)]

"""
a = 10
b = 20
c = 30
d = 40
e = 50
#result = a+b-c*d/e
#result = 10-2+2
result = 2 + (10*20) - (30/10)
print(result)
"""

                                             #||Numbers:||
#[+,-,*,/,//(floor division),%(modulus),**(exponentiation)]
"""
a = 10
b = 3
print(a + b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  #[floor division er kaj hoilo bhag sesher porer numbers gula ar show kre na.]
print(a**b)
print(a%b)
"""

                                             #||Mathmatics:||

#Square_root:
x = 10
print(math.sqrt(10))

#Math_functions:
"""
print(math.pow(10, 3))
print(math.sin(math.radians(90)))
print(math.cos(math.radians(90)))
print(math.tan(math.radians(45)))

print(math.factorial(5))  #5 factorial math: 5x4x3x2x1

print(math.gcd(48,100))   #[ল সা গু]

print(math.lcm(48,100))   #[গ সা গু]

print(math.fabs(-100))    #[poromman math]

print(math.floor(3.7))
print(math.ceil(3.7))

print(math.pi)    #[constant er math]
"""

a = 3.4444444
print(round(a,2))    #[bhag sesher pore koto ghor show krbe tar process]





















