# d/f b/w module & function & packages
# module -> a module in python is a single python file it consist python core.
# it tipically consist of functions, classes & variables that can be used in other puthon scripts or programs (or) contains pyhon code.
# examples of modules ->math.py, random.py (or) my module.py.

# Packages -> a package in python it is a diretory cantaining one (or) more python modules and an "__init__.py" file.
# The "__init__.py" file can be empty (or) contain intilization code for the package.
# enxamples of packages -> numpy, pandas, djongo & requestes.

# library -> it consists of both modules and packages.
# examples of library -> numpy, pandas & matplotlib.

# Note: every python file is module & import is a keyword & every python file is saved internally with variable name as "__main__".
# pyhton location -> C:\Users\User\AppData\Local\Programs\Python\Python314>

'''def greetings(name):
    print("welcome",name)'''

'''a=4
b=8
print(a+b)'''


'''a=int(input())
b=int(input())
print(a+b)'''

'''details={"idnos":[10,20,30],
        "names":["vijitha","srujana","yashu"],
        "marks":[98,99,99]}'''

'''if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.append("code")
    print(a)'''

'''def dummy():
    if __name__ == "__main__":
        print("this code is run as script")
    else:
        print("this program is run as module")
dummy()'''

# math modules
'''import math
print(math.pi)
print(math.pi*4)
print(math.sqrt(2))
print(math.log(2))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.pow(2,4))
print(math.ceil(6.9))
print(math.floor(3.11))'''

#from keyword
'''from math import pi,sqrt,log,tan
print(pi)
print(sqrt(4))
print(log(6))
print(tan(45))'''

# sys module
'''import sys
print(sys.version)
print(sys.path)'''

# os module
'''import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\User\\Downloads"))
print(os.listdir())'''

# random module -> is used to generate a random numbers in python randint function is used and this function is defined in random module
# sample -> random multiple numbers r mentioned numbers
# randint -> random single int
# choice -> we have to give some number and it will choose from that list or set or tuple

# random module()
'''import random
a = random.sample(range(10,40,5),5)
print(a)'''

# randint()
'''import random
a = random.randint(50,60)
print(a)'''

# choice()
'''import random
a = [30,40,50,60,70]
b = random.choice(a)
print(b)'''

# task

'''import random
while True:
    input("Enter the roll of dice: ")
    a = random.randint(1,6)
    print(a)
    b = input("roll again? (y/n): ")
    if b == "y":
        continue
    elif b == "n":
        break
    else:
        print("Invalid option")'''

# Calender module
'''import calendar
year = 2026
month = 8
print(calendar.month(year, month))'''

# year calender
'''import calendar
year = 2027
print(calendar.calendar(year))'''

'''import calendar
year = int(input("Enter the year: "))
print(calendar.calendar(year))'''

'''import calendar
a = int(input("year"))
b = int(input("month"))
print(calendar.month(a,b))'''

# Date & Time
'''from datetime import date
a = date.today()
print(a)'''

'''import datetime
a = datetime.datetime.now()
print(a)'''

# epoch time
'''import time
a = time.time()
#print(a)

b = time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"today time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"today day is {b.tm_yday}:{b.tm_wday}:{b.tm_isdst}")'''

# to generator ramdom numbers using time.sleep(2)
'''import random
import time
for i in range(10):
    a = random.choice(range(0,10))
    time.sleep(2)
    print(a)'''

# error handling 
""" syntax_error -> compilation error
run_time_error -> during execution time it will happens
logical_ error -> error in logic(in can't be visible)"""

# error handling
#syntax error
'''for i in range(10)
print(i)

for i in range(10):
print(i'''

#run_time_error
'''a = int(input())
b = int(input())
print(a//b) '''# 10/0 -> zero division error

# logical error
'''a = 10
b = 20
print(a-b)

a = 10
b = 20
if a>b:
    print("less")'''

# Expection Handling -> try, except, else, finally
'''try => Instructions from which we are expecting the exception.
except => Exceptions are raised in try block it will be handle by this block.
else => optional(no. exceptions)
finally => Always it will display'''

# Exception Handling
'''while True:
    try:
        a = int(input("A value: "))
        b = int(input("B value: "))
        c = a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("Program ends.....")'''

# Regex(Regular expression)
# They r powerful tools(bracket module)embedded in python which is mainly a given string(r)stmt(r)files and we mainly use it for text manipulation.
'''a = "codegnan is in vijayawada"
print(a)'''

'''a = "codegnan\nis\tin\nvijayawada"
print(a)'''

# rstring
'''a = "codegnan\nis\tin\nvijayawada"
print(a)'''

# compile(),search(),findall(),split(),sub()
# sequence characters
#\w => it matches alphanumeric
#\W => it matches non-alpha numeric
#\d => it matches any digit
#\D => it mathces non-digit
#\s => it represents white spaces
#\S => it repesents non-white spaces
#\b => it creates the boundary


# compile()
import re
#a = "mat cat maths money cash code cup dog donkey mug"
'''b = re.compile(r"m\w\w\w\w")
print(b)'''

# search()
'''c = b.search(a)
print(c)'''

'''b = re.search(r"m\w+", a)
print(b)'''

# findall()
'''c = re.findall(r"c\w+",a)
print(*c)'''

# split()
'''d = re.split(r"m",a)
print(d)''' 

'''e = re.split(r"\s",a)
print(e)'''

'''f = re.split(r"\S",a)
print(f)'''

# sub()
'''g = re.sub("m","a", a)
print(g)'''

