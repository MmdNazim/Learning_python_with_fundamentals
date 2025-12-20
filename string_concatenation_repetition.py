"""
#string repetition:
name = 'nazim '

repeat = name * 4

print(repeat)
"""

"""
#string concatenation:
str = 'hello'
str1 = 'nazim'

combine = str +" : "+ str1

print(combine)
"""

"""
#string concatenation with "join()" method:
a = 'ba'
b = 'ba'

connect = "". join([a, b]) + ":)"

print(connect)
"""

"""
#string concatenation with "format()" method:
a = 'ba'
b = 'ba'

connect = "{}{}:)".format(a, b)

print(connect)
"""

#string concatenation with "%(moduls)" method:
a = 'ba'
b = 'ba'

# connect = "%s %s:)" %(a, b)
connect = f"{a} {b} :)"     #[NOTE: this the way to formatintg your string / f'string]

print(connect)

