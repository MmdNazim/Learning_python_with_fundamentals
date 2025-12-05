                                              #||Create_directory/folder||
"""
import os
os.mkdir("Hello_Nazim")      #["mkdir = make directory" ei build-in function diye directory/folder ta create kra hoy]
"""

"""
import os
os.mkdir("nz")
"""

                                              #||Reading_a_directory/folder||
"""
import os
dirItems = os.listdir(".")
print(dirItems)
"""

                                              #||writing to a file in a directory/folder||
"""
with open("nz/test.text", "w") as file:
    file.write("hello pk")
"""
                                              #||Rename_directory/folder||
"""
import os
os.rename('Hello_Nazim', 'hello_namim')
print("Rename successfully")
"""

"""
import os 
os.rename("nz", "new")
print("rename successfully!")
"""

                                              #||Delete_directory/folder||
"""
import os
os.rmdir('hello_namim')     #["rmdir = remove directory" ei build-in function diye directory/folder ta remove kra hoy]
print("Done")
"""

"""
import os 
os.remove("j/i.text")      #[eikhane directory empty na thakar karone prothome directory te jei file ache take delete krar jonno ei kaj kra hyeche]
os.rmdir("j")              #[eikhane file delete kre then directory delete kra hyeche]
print("done")
"""

"""
import os 
os.remove("new/test.text") 
os.remove("new/w.text")      #[eikhane directory empty na thakar karone prothome directory te jei file ache take delete krar jonno ei kaj kra hyeche]
os.rmdir("new")              #[eikhane file delete kre then directory delete kra hyeche]
print("done")
"""




                                              #||Read files name from dictionry and print list/folder||
"""
import os 
fileList = os.listdir("new")
for file_name in fileList:
   print(file_name)
"""



