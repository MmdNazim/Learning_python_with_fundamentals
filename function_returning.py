#what is return: The "return" keyword is to exit a function and return a value. 

#function returning a single value:
"""
def addTwo(a, b):
    num1 = a
    num2 = b
    sum = num1 + num2
    return sum
result = addTwo(10,20)
print(result)
"""

#function returning a multiple values:
"""
def addTwo(a, b):
    num1 = a
    num2 = b
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return sum,sub,div,mul
result = addTwo(10,10)
print(result)
"""

#function returning nothing:
"""
def addTwo(a, b):
    num1 = a
    num2 = b
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    print(sum,sub,mul,div)


addTwo(10,10)
"""

#function returning a list:
"""
def addTwo(a, b):
    num1 = a
    num2 = b
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return [sum,sub,div,mul]
result = addTwo(10,10)
print(result)
"""

#function returning a list:
"""
def addTwo(a, b):
    num1 = a
    num2 = b
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return {"sum":sum,"sub":sub,"div":div,"mul":mul}
result = addTwo(10,10)
print(result)
"""

#using return for early exit:
"""
def first_even_number(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None

result = first_even_number([1,2,3,4,5,6,7,8,9,10])  #[eikhane function early return kre theme jabe porer gula ar check krbe na]

#result = first_even_number([1,3,5,7,9])     #[kinto eikhane puru loop ghurbe tarpore return krbe "None" ]

print(result) 
"""