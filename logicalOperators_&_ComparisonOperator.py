                                           #||Logical_operators:||
#1.And Operator 2.Or Operator 3.Not Operator 4.Combine Operator

#AND_operator:
"""
age = 20
nid_card = True

if age >= 18 and nid_card == True:
    print("you are consider as voter")
else:
    print("you are not consider as voter")
"""

"""
age = 17
has_permission = True

if age >= 18 and has_permission == True :    #[NOTE: eikhane and condition er kaj holo duita condition e true hoite hbe]
    print("you are old enough")
else :
    print("you are not old enough")
"""

#OR_operator:
"""
age = 17
nid_card = True

if age >= 18 or nid_card == True:
    print("you are a voter")
else:
    print("you are not a voter")
"""

"""
age = 20
has_permission = False

if age >= 18 or has_permission == True :    #[NOTE: eikhane OR condition er kaj holo duita condition er majhe ekta true holei full condition true hye jabe]
    print("you are old enough")
else :
    print("you are not old enough")
"""

#NOT_operator:
#Kono na buhok kichu krte hoile amra "NOT" operator use krbo.
"""
age = 2
if not age >= 18:
    print("you are child")
else:
    print("you are adult")
"""

"""
age =  12

if not age >= 18 :
    print("you are adult")
else :
    print("you are not adult")
"""    


#Combining logical operators:
#[NOTE: Combine logical operator condition apply krar time juray juray boshe]
"""
age = 20
passport = True
isBangladeshi = True
nid_card = True
gender = "Female"

if (age >= 18 and passport == True) and (isBangladeshi == True or nid_card == True) and gender == "Male":
    print("you can vote")
else:
    print("you can not vote")
"""

"""
age = 20
has_permission = False
is_vip = False

if (age >= 18 and  has_permission) or is_vip :
    print("join my club")
else :
    print("can not join my club")
"""    




                                           #||Comparison_operators:||
#1.Equal to (==) 2.Not Equal to (!=) 3.Greater than (>) 4.Less than (<) 5.Greater than or equal (>=) 6.Less than or equal (<=)

#Equal to (==):
"""    
a = 4
b = 5

print(a == b)
"""  

#Not Equal to (!=):
""" 
a = 4
b = 5

print(a != b)
""" 

#Greater than (>):
""" 
a = 4
b = 5

print(a > b)
""" 

#Less than (<):
""" 
a = 4
b = 5

print(a < b)
""" 

#Greater than or equal (>=):
""" 
a = 4
b = 5

print(a >= b)
""" 

#Less than or equal (<=):
""" 
a = 4
b = 5

print(a <= b)
""" 