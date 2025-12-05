#local variable: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
"""
def myFun():
    x = 10     #[local variable]
    y = 20     #[local variable]
    print(x+y)

myFun()

print(x+y)     #[out of scope theke access krar try kra hyeche kinto access kra jacche na]
"""

#global variable: Variables that are created outside of a function are known as global variables.Global variables can be used by everyone, both inside of functions and outside.
"""
x = 10     #[global variable]
y = 20     #[global variable]

def myFun():

    print(x+y)

myFun()

print(x+y)     #[out of scope thekeo access kra jacche tai take global variable bole]
"""

#local and global variables with same name:
"""
text = "hello i am global"   #[global variable]

def myfun():
    text = "hello i am local"     #[local variable]
    print(text)      #[eikhane jei "text" ke print krlam oita access krte parbe "local variable" ke]

myfun()

print(text)          #[eikhane jei "text" ke print krlam oita access krte parbe "global variable" ke]
"""

#modifying global variables inside a function:
"""
x = 10

def sum1():
    global x    #[eikhane "global" keyword use kre local e "x = 20" new ei variable ta assign kra hyeche, jeita gobal variable "x = 10" ke change kre jeita new add kra hyeche oita assign hbe - ar eivabei global variable ke modify kra jay]
    x = 20
    # x = 20   #[locally variable declar krlam eita only locally variable ke change krbe]
    result = x + 1
    print(result)

sum1()


def sum2():
    result = x + 2
    print(result)

sum2()
"""