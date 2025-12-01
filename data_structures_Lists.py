                                                #||List_Methods:||
#List related method niye eikhane study krbo. 

#List allow duplicate value:
"""
fruits = ['apple', 'apple', 'banana', 'cherry', 'cherry']
print(fruits)
"""

#List_indexing_code:
"""
city = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong"]
print(city[3])
print(city[2])
"""

#append()_method:
#eikhane "append()" method ta use kre list er seshe kono new item add kra jay.
"""
city = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong"]
city.append("Cox's Bazar")
print(city)
"""

#insert()_method:
#eikhane "insert()" method use kre list er specific position e amra item add krte pari.
"""
city = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong"]
city.insert(2,"Cox's Bazar")
print(city)
"""

"""
fruits = ['apple', 'apple', 'banana', 'cherry', 'cherry']
fruits.insert(2,'mango')
print(fruits)
"""

#extend()_method:
#eikhane "extend()" method ta diye amra duita list ke eksathe jura lagate pari.
"""
city1 = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong"]
city2 = ["Cox's Bazar", "Khulna", "Comilla", "Barisal", "Chittagong"]
city1.extend(city2)

print(city1)
"""

"""
fruits = ['apple', 'banana', 'cherry']
more_fruits = ['grape', 'melon', 'pineapple']

fruits.extend(more_fruits)

print(fruits)
"""

#remove()_method:
#eikhane "remove()" method use kre specific kono position theke item remove kra jabe.
"""
city = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong"]
city.remove("Chittagong")

print(city)
"""
"""
fruits = ['apple', 'apple', 'apple', 'banana', 'cherry']         #[NOTE: Remove the first occurence of the specified elements]
fruits.remove('apple')

print(fruits)
"""

#pop()_method:
#eikhane "pop()" method use kre list er last item ke remove/delete krte pari.
"""
city = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong"]
city.pop()

print(city)
"""

"""
fruits = ['apple', 'banana', 'cherry']
fruits.pop()  #[NOTE: pop() method always list er last element ke delete kre]

fruits.pop(1)  #[NOTE: pop() method diye jdi onno element ke delete krte hoy then oi element er index number diye call krte hbe]

print(fruits)
"""
 

#clear()_method:
#eikhane "clear()" method use kre list er shob element clear kre felbe and output e faka list show krbe.
"""
city = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong"]
city.clear()

print(city)
"""

"""
fruits = ['apple', 'banana', 'cherry']
fruits.clear()

print(fruits)
"""

#index()_method:
#eikhane "index" method ta use kre specific item er index count ta koto ta jana jay.
"""
city = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong"]
print(city.index('Comilla'))
"""

"""
fruits = ['apple', 'banana', 'cherry']
indexNo = fruits.index('banana')

print(indexNo)
"""

#count()_method:
#Eikhane "count()" method ta use kre list er majhe duplicate item koto bar ache tar count kra jay.
"""
city = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong", "Dhaka", "Dhaka"]
print(city.count('Dhaka'))
"""

"""
fruits = ['apple', 'apple', 'apple', 'banana', 'cherry'] 
elementCount = fruits.count('apple')

print(elementCount)
"""

#sort()_method:
#eikhane "sort()" method use kre je kono item ke jdi ascending order e shajate pari.
"""
numbers = [3,4,7,74,45,755,345,5466,45,23,656,1,3,4,2]
numbers.sort()

print(numbers)
"""

"""
fruits = ['banana', 'cherry', 'apple', 'apple', 'apple'] 
fruits.sort()     #[NOTE: sort() method by default acending order e kaj kre]

print(fruits)
"""

#reverse()_method:
#eikhane "reverse()" method ta use kre item ke reverse e show kra jay.
"""
numbers = [8,5,7,74,45,10,23,6,1,3,4,2,9]
numbers.sort()
numbers.reverse()

print(numbers)
"""

"""
fruits = ['apple', 'apple', 'apple', 'banana', 'cherry']
fruits.reverse()

print(fruits)
"""

#len()_method:
#eikhane "len()" use kre list er bitore koto gula item ache tar length ber kra jay.
"""
numbers = [8,5,7,74,45,10,23,6,1,3,4,2,9]
print(len(numbers))
"""

"""
fruits = ['apple', 'fig', 'date', 'banana', 'cherry', 'grape']
length = len(fruits)

print(length)
"""

#slicing_method:
"""
city = ["Dhaka", "Khulna", "Comilla", "Barisal", "Chittagong", "Cox", "Rangpur"]
print(city[:3])  #First_cut  #[eikhane jei pashe number thakbe list er oi pashta kata jabe ar joto number thakbe list er shamner toto item e show krbe.]
print(city[1:5])  #middle_cut
print(city[4:])   #last_cut   #[eikhane jei pashe number thakbe list er oi pashta kata jabe ar joto number thakbe list er start theke toto items remove kre baki item gula show krbe.]
"""

"""
fruits = ['apple', 'fig', 'date', 'banana', 'cherry', 'grape']

print(fruits[1:4])
print(fruits[:4])    #[NOTE: by default 0 teke count kra start krbe]
print(fruits[4:])    #[NOTE: 4 theke start kre list er last porjhonto count krbe]
print(fruits[-3:])   #[NOTE: "-3", diye olta dik theke start kre list er last porjhonto count kre print krbe like, fruits = ['apple(-6)', 'fig(-5)', 'date(-4)', 'banana(-3)', 'cherry(-2)', 'grape(-1)']]
"""

#Looping through a list:

"""
fruits = ['apple', 'fig', 'date', 'banana', 'cherry', 'grape']

for eachFruit in fruits:
    print(eachFruit)
"""


#[NOTE:List of use case: 1.shopping cart 2.To Do lists 3.storing 4.analysis [uporer method gula ei shob kaje use krte pari.]