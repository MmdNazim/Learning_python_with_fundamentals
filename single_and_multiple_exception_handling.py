#NOTE:
"""
exception handling: When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

-> The try block lets you test a block of code for errors.

-> The except block lets you handle the error.

-> The else block lets you execute code when there is no error.

-> The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

#simple try exception handling/single exception handling:
"""
try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    # print("Division by zero")   #[eikhane normal message print kra hyeche]

    print(ZeroDivisionError)      #[eikhane amra je error handling krechi sheita eivabe print krte pari]
"""

#multiple exception handling: 
"""
try:

 with open("new.text", 'r') as file:
    content = file.read()
    result = 10/int(content)
    print(result)

except FileNotFoundError:
 print("file not found")

except ValueError:
  print("ValueError")

except TypeError:
  print("TypeError")

except ZeroDivisionError:
  print("ZeroDivisionError")
"""

#catching all exception handling/this the best practice way to exception handling[I follow this way]:

try:

 with open("new.text", 'r') as file:
    content = file.read()
    result = 10/int(content)
    print(result)

except Exception as e:
  print(e)


#finlly block in single exception handling:
"""
try:
   result = 10/0
   print(result)
except ZeroDivisionError:

    print(ZeroDivisionError)
finally:
    print("Excecuted complete")
"""

#finlly block in multiple exception handling:
"""
try:

 with open("new.text", 'r') as file:
    content = file.read()
    result = 10/int(content)
    print(result)

except FileNotFoundError:
 print("file not found")

except ValueError:
  print("ValueError")

except TypeError:
  print("TypeError")

except ZeroDivisionError:
  print("ZeroDivisionError")

finally:
    print("Excecuted complete")
"""


#finally block in catching all exception handling/this the best practice way to exception handling for indrustry level[I follow this way]:

try:
    with open("new.text", 'r') as file:
        content = file.read()
        result = 10/ int(content)
        print(result)

except Exception as e:
    print("error found:", e)

finally:
    print("execution completed")
