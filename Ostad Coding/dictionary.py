#NOTE:
#dictionary "{}" er majhe thakbe 
#dictionary "key value" pair e thake 
#dictionay te index dhore kaj krar shujog nai
#dictionary r key gula obossoi immutable hoite hbe

"""
a = {'tamim' : 12, 'karim' : 14, 'fahin' : 78, 1:[1,2,3,4], 2:{3,4,5}}

print(type(a))
for item in a:
    print(item)
"""

# print("---------------------------------")
"""
for i in a.values():
    print(i)

print(a.keys(), a.values())     #[eikhane keys and values pair ta list akare pawa jay]
"""

# print("---------------------------------")
"""
# #eksathe jodi key and value gula dekhanur jonno ei rules:
for k,v in a.items():
    print(f"key name: {k}, values {v}")
"""

#print("---------------------------------")
"""
a = [1,2,3]
b = ["mango", "banana", "apple"]

#[duita set theke ekta dictionary bananur process "like:{1:mango, 2:banana, 3:apple}"]
 
c =  dict(zip(a,b))  #[eikhane key ber krar time of course "zip(a,b)" ei function tar upor nirvor krbe]
print(c[1])   #[eikhane just alada kre rekhe key gula ber krte pari || eikhane key  lekhar time obossoi "zip(a,b)" dekhe lekhte hbe na hoy error dibe]

print(dict(zip(a,b)))  #[eikhane "zip()" ta diye hocche uporer duita list ke eksathe kre tarpore "dict()" ta diye dictionary te convert kra hyeche]



d =  dict(zip(b,a))   #[eikhane key ber krar time of course "zip(b,a)" ei function tar upor nirvor krbe]
print(d["mango"])     #[eikhane just alada kre rekhe key gula ber krte pari || eikhane key lekhar time obossoi "zip(b,a)" dekhe lekhte hbe na hoy error dibe]
"""