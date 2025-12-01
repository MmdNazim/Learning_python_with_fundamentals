                                            #||Tuple_Methods:||

#👉tuple behave kre "list" er moton kre. tara dui jon same.

#count() method: 👉tuples er ei method diye specific ekta value koto bar royeche sheita counting kra jay.

"""
numbers = (2,2,3,5,4,6,7,1)
specificValueCount = numbers.count(2)

print(specificValueCount)
"""

"""
gf = ('a', 'b', 'c', 'd', 'a', 'a')
print(gf.count('a'))    #[eikhane "count()" ta duplicate value koto bar ache ta count kre]
"""

#index()_method: 👉 eikhane "index()" method always variable r majhe je value assign krechi tar position bole, ba amra ei method use kre variable theke specific item er position ber krte pari.
"""
gf = ('a', 'b', 'c', 'd')
serial = gf.index('c')    

print(serial)
"""

"""
fruits = ('apple', 'banana', 'cherry')
valueIndex = fruits.index('banana')

print(valueIndex)
"""

#tuple_er_majhe_for_loop_use_kre_all_item_one_by_one_show_krte_hoy_tahole_ei_process:
"""
allGf = ( "jorina", "sokhina", "katrina" )
for oneGf in allGf:    #[eikhane "for loop" chalanu hoise]
    print(oneGf)
"""

"""
fruits = ('apple', 'banana', 'cherry', 'fig', 'mango', 'melon')

for item in fruits:
    print(item)
"""

#tuple_to_list_conversion: 👉 eikhane tuples ke list e convert kra jay
"""
gf = ('a', 'b', 'c')
tuple_gf_covert_list = list(gf)

print(tuple_gf_covert_list)
"""

"""
fruits = ('apple', 'banana', 'cherry')
fruitsList = list(fruits)

print(fruitsList)
"""

#Tuple slicing:
"""
fruits = ('apple', 'banana', 'cherry', 'fig', 'mango', 'melon')

print(fruits[1:3])
print(fruits[1:])
print(fruits[:3])
print(fruits[-2:])
"""



#Tuple use case:
#- as like as list.