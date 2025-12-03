                                               #||Sets_Methods:||
#Sets always unique value niye kaj kre. sets er majhe jdi duplicate value assign hoy ta "print" er time e ekbar e show kre.

#The way of finding memory location:

"""
fruits = {'apple', 'banana', 'cherry'}

print(id(fruits))
fruits.add('date')
print(fruits)
print(id(fruits))
"""

#Duplicate value avoid kre and Unique value return kre:
"""
girlFriends = { "jorina", "sokhina", "katrina", "katrina"}    #[sets always unique value return kre.]
print(girlFriends)
"""

#add_method:
"""
girlFriends = { "jorina", "sokhina", "katrina" }
girlFriends.add("rohima")      #[eikhane "add()" use kre new item add kra hyeche sets e.]

print(girlFriends)
"""

"""
fruits = {'apple', 'banana', 'cherry'}

fruits.add(1)
print(fruits)
"""

#remove()_method:
"""
girlFriends = { "jorina", "sokhina", "katrina" }
girlFriends.remove("jorina")      #[eikhane "remove()" use kre specific item remove kra hyeche.]

print(girlFriends)
"""

"""
fruits = {'apple', 'banana', 'cherry'}

fruits.remove('cherry')
print(fruits)
"""

#discard()_method:
"""
girlFriends = { "jorina", "sokhina", "katrina" }
girlFriends.discard("jorina")     #[eikhane "discard()" method diye remove er kaj kra hoy. ar ei duita method like "discard()" and "remove()" method same kaj kre.]

print(girlFriends)
"""

#update()_method:
"""
girlFriends = { "jorina", "sokhina", "katrina" }
girlFriends.update(["sokhina", "sarika"])      #[eikhane "update()" use kre specific item er jaigay add kra hyeche.]

print(girlFriends)
"""

"""
fruits = {'apple', 'banana', 'cherry'}
fruits.update(['date', 'melon'])

print(fruits)
"""

#clear_method:
"""
girlFriends = { "jorina", "sokhina", "katrina" }
girlFriends.clear()      #[eikhane "clear()" method er kaj holo shob item sets theke delete kre faka/khali sets return kre]

print(girlFriends)
"""

"""
fruits = {'apple', 'banana', 'cherry'}

fruits.clear()
print(fruits)
"""

#union method: 👉Ei method diye amra duita sets ke jura lagate pari
"""
set1 = {1,2,3,4}
set2 = {5,6,7,8}

unionSet = set1.union(set2)

print(unionSet)
"""

"""
set1 = {1,2,3,4}
set2 = {4,5,6,7}      #[NOTE: sets kokhono duplicate value return kre na]

unionSet = set1.union(set2)

print(unionSet)
"""

#intersection method: 👉Ei method diye duita sets er majhe common jei item gula ache shei guli count kre return kre
"""
set1 = {1,2,3,4}
set2 = {4,5,6,7,2}    

value = set1.intersection(set2)

print(value)
"""

#difference method:
"""
set1 = {1,2,3,4}
set2 = {4,5,6}

value = set1.difference(set2)
# v1 = set2.difference(set1)

print(value)
# print(v1)
"""

#issubset method: 👉 Every element of Set A must exist inside Set B.If all elements of one set are present inside another set,then that set is a subset.
"""
set1 = {1,2,3,4}
set2 = {4,5,6}

value = set1.issubset(set2)


print(value)
"""

#issuperset method: 👉 Set A contains every element of Set B — plus maybe more.
"""
set1 = {1,2,3,4}
set2 = {4,5,6}

value = set1.issuperset(set2)


print(value)
"""


#sets use case:
#-unique value niye kaj kre.

#Important NOTE:
"""
✅ 1. difference(): What is in Set A but NOT in Set B.

✅ 2. symmetric_difference(): What is NOT common between A and B. Everything that is unique to each set.

👍 Best Way to Remember:

➡ difference() = Only my items (A’s unique items)

➡ symmetric_difference() = Unique from both sides (A’s uniques + B’s uniques)
"""