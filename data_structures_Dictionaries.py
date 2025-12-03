                                             #||Dictionary_Methods:||
#specific_item:
"""
address = {
    'city' : 'dhaka',
    'area' : 'adabor',
    'location' : 'japan city garden',
    'building' : 20,
    'flat' : 901
}
print(address['location'])
"""

#keys() & values()_method:
"""
address = {
    'city' : 'dhaka',
    'area' : 'adabor',
    'location' : 'japan city garden',
    'building' : 20,
    'flat' : 901
}
#'city' : 'dhaka'[eikhane 'city' = key and 'dhaka' = value]
print(address.keys())
print(address.values())
"""

"""
person = {
    "name" : "Nazim",
    "age" : 27,
    "city" : "comilla",
    "isBangladeshi" : True
}

print(person.keys())
print(person.values())
"""

#items_method:
"""
person = {
    "name" : "Nazim",
    "age" : 27,
    "city" : "comilla",
    "isBangladeshi" : True
}

print(person.items())
"""

#update()_method:
"""
address = {
    'city' : 'dhaka',
    'area' : 'adabor',
    'location' : 'japan city garden',
    'building' : 20,
    'flat' : 901
}
print(address.update({'flat' : 902}))  #[eikhane specific kono item ke update er jonno eita use kra hoy.]
print(address)
"""

"""
person = {
    "name" : "Nazim",
    "age" : 27,
    "city" : "comilla",
    "isBangladeshi" : True
}

person.update({"city" : "dhaka"})

print(person)
"""

#pop()_method:
"""
address = {
    'city' : 'dhaka',
    'area' : 'adabor',
    'location' : 'japan city garden',
    'building' : 20,
    'flat' : 901
}
address.pop('city') #[Eikhane individual item ke "pop()" method use kre delete kra jay.]
address.pop('area')
address.pop('location')
address.pop('building')
address.pop('flat')

print(address)
"""

"""
person = {
    "name" : "Nazim",
    "age" : 27,
    "city" : "comilla",
    "isBangladeshi" : True
}

x = person.pop("name")   #[NOTE: eikhane pop() method diye kono property ke delete krle pore pop() tar value return kre]

print(person)
print(x)
"""

#clear()_method:
"""
address = {
    'city' : 'dhaka',
    'area' : 'adabor',
    'location' : 'japan city garden',
    'building' : 20,
    'flat' : 901
}
address.clear()  #[Eikhane ei "clear()" method ta use kre shob gula item ke clear kre dewa jay dictionary theke.]
print(address)
"""

"""
person = {
    "name" : "Nazim",
    "age" : 27,
    "city" : "comilla",
    "isBangladeshi" : True
}

person.clear()

print(person)
"""

#get()_method:
"""
romna = {
    "girl1" : "boy1",
    "girl2" : "boy2",
    "girl3" : "boy3",
    "girl4" : "boy4",
    "girl5" : "boy5",
    "girl6" : "boy6",
    "katrina" : "SK"
}

search_katrina = romna.get("katrina", 'Not Available')  #[eikhane "get()" method ta use kre specific item ke search diye ber kre niye asha jay.]
print(search_katrina)
"""

"""
person = {
    "name" : "Nazim",
    "age" : 27,
    "city" : "comilla",
    "isBangladeshi" : True
}


print(person.get("name"))
"""

#copy()_method:
"""
romna = {
    "girl1" : "boy1",
    "girl2" : "boy2",
    "girl3" : "boy3",
    "girl4" : "boy4",
    "girl5" : "boy5",
    "girl6" : "boy6",
    "katrina" : "SK"
}
nee_romna = romna.copy()   #["copy()" method diye arekta ek e rokom dictionary craete kra jay]
print(nee_romna)
"""

#Jason_array:
"""
dhaka = {         #[eikhane specific couple set like "dhaka"  ke "jason object" bola hoy.]
    "girl1" : "boy1",
    "girl2" : "boy2",
    "girl3" : "boy3"

}

jahangirnagar = {     #[jason object]
    "girl1" : "boy1",
    "girl2" : "boy2",
    "girl3" : "boy3"

}

khulna = {            #[jason object]
    "girl1" : "boy1",
    "girl2" : "boy2",
    "girl3" : "boy3"

}
keep_all = [dhaka, jahangirnagar, khulna]    #[eikhane alada alada dictionary ke eksathe print krake "jason array" bole.]
print(keep_all)
"""

#Using_for_loop_separate_keys_&_values:
"""
address = {
    'city' : 'dhaka',
    'area' : 'adabor',
    'location' : 'japan city garden',
    'building' : 20,
    'flat' : 901
}

for key, value in address.items():
    print(f"key is {key} and value is {value}")   #[eikhane print er majhe (f"") eivabe likha hoiche tar meaning hocche string formatting kra]
"""









