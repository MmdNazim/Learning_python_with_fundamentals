                                           # ||Immutable_Data_Type||
"""
#List_type_example:
l = [1,2,3,4]
firstLocation = id(l)
l[0] = 5  #eikhane index dhore value ta change kra hyeche.
secondLocation = id(l)

print(firstLocation)
print(secondLocation)
"""

"""
#Dictionaries_type_example:
d = {'a': 1, 'b' : 2}
firstLocation = id(d)
d['b'] = 3
secondLocation = id(d)

print(firstLocation)
print(secondLocation)
"""

#Sets_type_example:
s = {1,2,3}
firstLocation = id(s)
s.add(4)    #eikhane "add" function use kre ekta element add kra hyeche.
secondLocation = id(s)

print(firstLocation)
print(secondLocation)

