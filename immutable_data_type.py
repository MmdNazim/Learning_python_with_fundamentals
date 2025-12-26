                                        #||Immutable_Data_Type||
"""
#Integer Example:
a = 2
first_location = id(a)  #eikhane memory r location trace krar jonno "id" namer method ta use kra hyeche.And tar majhe object ta pass kra hyche.
a = 3
second_location = id(a)
a = 5
#Note: eikhane "a" er value different different asign kra hyeche tar mane ei na je "a" er value ekta baad hye arekta add hyeche. eikhane memory te "a" er value gula different different location create kreche.
third_location = id(a)

print(first_location)
print(second_location)
print(third_location)
"""

"""
#Floating point numbers Example:
a = 3.1416
first_location = id(a)
a = 9.8
second_location = id(a)

print(first_location)
print(second_location)
"""

"""
#String Example:
a = "hello"
first_location = id(a)
a = "nazim"
second_location = id(a)

print(first_location)
print(second_location)
"""

"""
#Tupels Example:
a = (1, 2, 3)
first_location = id(a)
a = (1,2,3,4)
second_location = id(a)

print(first_location)
print(second_location)
"""

#Frozenset Example:
a = frozenset([1,2,3,4])
first_location = id(a)
a = frozenset([1,2,3,4,5,6])
second_location = id(a)

print(first_location)
print(second_location)
