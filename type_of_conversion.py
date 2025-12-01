#Explicit Conversion: 👉 You manually convert one data type into another using built-in functions.
"""
a = 32
b = int(a)
c = float(a)
d = str(a)

print(b)
print(c)
print(d)
"""

#Implicit conversion: 👉 Python automatically converts one data type to another when needed. You don’t have to convert it manually.
"""
x = 34
y = 4.34
z = x + y

print(z)
"""

#Handling conversion error:
"""
try:
    name = 'Nazim'
    x = int(name)
    print(x)

except Exception as e:
    print(e) 
"""
