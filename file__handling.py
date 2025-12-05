#create file:
"""
with open('example.text','w') as file:
    print("created") 
"""

#write file:
"""
with open('example.text','w') as file:
    file.write("hello python world")
"""

#read file:
"""
with open("example.text", "r") as file:
    content = file.read()
    print(content)
"""

#rename file:
"""
import os    #[ei "import os" must krte hbe]

os.rename("example.text", "example2.text")
"""

#remove file:
"""
import os    #[ei "import os" must krte hbe]

os.remove("example2.text")      #[this the way, jodi file ta same folder e thake then eivabe remove krte pari]
os.remove("test/r.text")        #[this the way, jodi file ta alada folder e thake tahole oi folder dhore and filer name shoho path ciniye eivabe deleter kaj sesh krte hbe]
"""
