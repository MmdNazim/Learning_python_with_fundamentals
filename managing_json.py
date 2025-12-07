"""
key functions:
-json.dumps(): ei function er kaj holo json object/dictionary boli take string ke convert krte pare
-json.loads(): ei function ta json string ke python object e convert kre.

-json.dump(): ei function ta python object ke json string file majhe rekhe write krte pare.
-json.load(): ei function ta json string er kono file ke read krte pare and file take python object e convert krte parbe.
"""



#python object ----> json string:
"""
import json
personOBJ = {
    "name" : "Nazim",
    "age" : 27,
    "city" : "comilla",
    "isBangladeshi" : True,
    "hasChildern": False,
    "titles": ["engineer", "programmer"]
}

personJSON = json.dumps(personOBJ, indent=4)  #[NOTE: pretty mode]
print(personJSON)
"""

#json string ----> python object:
"""
import json

personJSON = '{"name" : "Nazim", "age" : 27, "city" : "comilla", "isBangladeshi" : true, "hasChildern": false, "titles": ["engineer", "programmer"]}'

personOBJ = json.loads(personJSON)

print(personOBJ)
print(personOBJ['name'])
"""

#python object ----> json string + file write:
"""
import json
personOBJ = {
    "name" : "Nazim",
    "age" : 27,
    "city" : "comilla",
    "isBangladeshi" : True,
    "hasChildern": False,
    "titles": ["engineer", "programmer"]
}

with open("person.json", "w") as personJSONFile:
    json.dump(personOBJ, personJSONFile, indent=4)    #[NOTE: pretty mode apply kra hyeche] 
"""

#json file read kre ----> python object ----> then json string e convert krbo:

import json
with open("person.json", "r") as personOBJFile:
    personOBJ = json.load(personOBJFile)
    print(personOBJ)       #[eikhane python object peyechi]
    print(personOBJ["age"])  #[eivabe amra single object print krte pari]

    personJSON = json.dumps(personOBJ, indent=4)   #[eikhane json string print krlam sathe pretty mode apply kre]
    print(personJSON)


