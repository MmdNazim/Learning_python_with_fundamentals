#function parameters and arguments:

"""
def addTwo(a, b):   #[eikhane parameters pass krlam]
    num1 = a
    num2 = b

    print(num1 + num2)

addTwo(2, 3)       #[eikhane arguments pass krlam]
addTwo(123, 234)
"""

#Required parameters:

"""
def addTrio(a, b, c):   #[eikhane parameters pass krlam duita ei duitar e value pass krte hbe]
    num1 = a
    num2 = b
    num3 = c

    print(num1 + num2 + num3)

addTrio(2, 3, 4)
"""

#default parameters:

"""
def addTwo(a, b = 100):   #[eibhabe amra default parameters set krte pari]
    num1 = a
    num2 = b

    print(num1 + num2)

addTwo(2)     #[]
"""

"""
def addTwo(a, b = 100):   #[eibhabe amra default parameters set krte pari]
    num1 = a
    num2 = b

    print(num1 + num2)

addTwo(2, 3)     #[jodi amra default value set kre abar arguments jeye default jei value ta set krechi tar value assign kri tahole ami arguments e je value ta assign krbo oi value ta count hbe, default value count hbe na]
"""

#variable length arguments: jokhn amra 'tuples' akare pathay tokhn boli "variable length arguments"

"""
def addTwo(*numbers):     #[NOTE: eikhane "*numbers" diye dynemic parameters pass krte pari, tai kra hyeche. ar eita tuples hishabe kaj kre]
    for number in numbers:
     print(number)

addTwo(5, 4, 399, 2, 3)        #[ar eita HETEROGENEOUS hishabe kaj kre, eikhane shokol data type er data pathanu jabe]
"""

#keywords arguments: jokhn amra "dictionary" akare pathay tokhn boli "keywords arguments"

"""
def hello(**person):   #[NOTE: eikhane "**person" double'**' diye dictionary akare data pass krte pari]
    for key, value in person.items():

        print(f'{key}:{value}')     #[NOTE: eikhane eikhane string formatting kre "key" ar "value" data ana hyeche]
        print(key +":"+ str(value)) 
    
    
    # print(person ["age"])  #[NOTE: eikhane specific item ber krte caile eivabe ber krte pari]

hello(
    name = "nazim",
    age = 28,
    city = "san francisco"
)
"""