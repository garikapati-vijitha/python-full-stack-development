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
