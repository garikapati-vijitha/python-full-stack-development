# FUNCTIONS
# a function is a block of organised, reusable code, and that is used to perform a single or multiple task.
# python gives in-built functions like print, and u can make ur own function also and this r called user defined functions.
# python blocks begin with the key word def followed by the function name and paranthesis "(())"
# by using the funtion we can decrease the length, and the to many print stmt, input variables.
# a function call by itself is called recursive function

# difference b/w print() and return 
# print()-> just shows the human user input in a console
# return -> return will terminate the function and give by the value from the function
#           single output and then it will terminate it self
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''


# def funtion
# sum, diff, product of number
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

# integer division, power, modulus of number
'''def calculate(a,b):
    print("the integer division is",a//b)
    print("the power is",a**b)
    print("the modulus is",a%b)
calculate(2,3)
calculate(4,2)
calculate(6,8)'''

# add
'''def add(a,b):
    print(a+b)
add(4,5)'''

# add using while loop, function
'''while True:
    def cal():
        a=int(input("a value: "))
        b=int(input("b value: "))
        print(a+b)
    cal()'''

# add using recursion, function
'''def cal():
    a=int(input("a value: "))
    b=int(input("b value: "))
    print(a+b)
    cal()
cal()'''

#fullname using function
'''def fullname():
    fname = input("enter first_name:")
    sname = input("enter second_name:")
    print((fname+""+lname).title())
fullname()'''

# return v/s print()
'''def mul(a,b):
    print(a*b)
mul(3,5)'''

'''def mul(a,b):
    return a*b
print(mul(2,4))'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(2,3)'''

# it won't print  o/p  cause we didn't use 
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
add(2,5)'''

# here the first return will print and the next will terminate
# first 1 will print because we used print in the program
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
print(add(2,5))'''

# Real life example
# splitbill()
'''def splitbill():
    a=int(input("Enter the bill: "))
    b=int(input("Enter the number of person's: "))
    c=a/b
    print(c)
splitbill()'''
# splitbill() using f string
#method 1
'''def splitbill():
    a=int(input("Enter the bill: "))
    b=int(input("Enter the number of person's: "))
    c=a/b
    print(f"The splited bill is: ",c)
splitbill()'''

#method 2
'''def splitbill():
    a=int(input("Enter the bill: "))
    b=int(input("Enter the number of person's: "))
    c=a/b
    print(f"The splited bill is: {c}")
splitbill()'''



# splitbill() using .format
'''def splitbill():
    a=int(input("Enter the bill: "))
    b=int(input("Enter the number of person's: "))
    c=a/b
    print("The splited bill is: {}".format(c))
splitbill()'''

# add, sub,mul
'''while True:
    def calculation():
        a=int(input("a value: "))
        b=int(input("b value: "))
        option=int(input("option 1.add 2.sub 3.mul"))
        if option == 1:
            print(a+b)
        elif option == 2:
            print(a-b)
        elif option == 3:
            print(a*b)
        else:
            print("Invaild option")
    calculation()'''

# multiple keyword
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value: "))
    b=int(input("b value: "))
    option=int(input("option 1.add 2.sub 3.mul"))
    if option == 1 :
        add()
    elif option == 2:
        sub()
    elif option == 3:
        mul()'''

# keyword and position arguments
 
'''def Details(id,name,mailid):
    id=1
    name="vijitha"
    mailid="v@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''# step1


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=1,name="vijitha",mailid="v@gmail.com")
Details(id=2,name="srujana",mailid="s@mail.com") # step2
Details(3,"yashu","y@gmail.com")#step3
Details("sunitha","su@gmail.com",4)#step4
Details(mailid="v@gmail.com",id=4,name="vijitha")'''#step5

# default arguments
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",100)'''

'''def Grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''

'''def Grocery(item="ghee",price):
    # non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(2000)'''

# real life project
# cake_name,price,qty
'''def Bakery(cake_name="vennila",price=200,qty=1):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg/g" %qty)
Bakery()'''

'''def Bakery(cake_name,price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg/g" %qty)
Bakery(cake_name="butter scotch",price=200,qty=1.5)'''

'''def Bakery(cake_name,price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg/g" %qty)
Bakery(200,2)'''# error

'''def Bakery(cake_name,price=500,qty=3):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg/g" %qty)
Bakery(butter scotch)'''

# *(star) arguments (* is used to unpack the elements)
'''a=[2,3,4,5,6,8,9]
print(a)
print(*a)'''

'''a=(2,3,4,5,6,8,9)
print(a)
print(*a)'''

'''a={2,3,4,5,6,8,9}
print(a)
print(*a)'''

'''b={"name":"vijitha","city":"vij"}
print(b)
print(*b)'''

'''c="python"
print(c)
print(*c)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''# error

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(*c)'''

'''*a,b,*c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(*c)''' # error

'''a,b,c="vijitha"
print(a)
print(b)
print(c)''' #error

'''a,b,c="vij"
print(a)
print(b)
print(c)'''

'''a,b,*c="vijitha"
print(a)
print(b)
print(*c)'''

# VARIABLE LENGTH ARGUMENT
# VARIBLE LENGTH ARUGUMENT AUTOMATICALY STORE IN TUPLE AND WE USE * ARGUMENTS

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8,9)
b=[4,5,6,7,8]
check(*b)
c={1,2,3,4,5,6,7,8}
check(*c)
d={"name":"vijitha","age":21,"place":"vja"}
check(*d)'''

'''def check1(*a):
    d=1 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d = d+i
            print(d)
check1()
check1(1,2,3,4,5,6,7,8)
check1(4,3,6,2.3,45.7)
check1(4,3,6,2.3,45.7,"python")'''
        
# ** (kwargs)
# keyword variable length arguments
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details = {"names":["sweety","suji","viji","suni"],
           "marks":[80,81,82,83]
           "status":["p","a","p","a"]}
check2(**details)'''

'''def check3(**a):
    print(a)
    print(type(a))
    for i in a: 
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check3()
details = {"names":["sweety","suji","viji","suni"],
           "marks":[80,81,82,83],
           "status":["p","a","p","a"]}
check3(**details)'''

# both * & ** usage in 1 program
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+1
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6,2.3,4.5)
# final(*data) """this is for single print of data but for details we need print the another line"""
details={"year":[2024,2026,2028],
         "month":["june","july","sept"]}
# final(**details) """this is for single print of details but for data we need print the another line"""
final(*data,**details)'''

# Railway Ticket
'''while True:
    def Railway():
        Gender = input("Enter the Gender: ")
        t=int(input("Enter the price of ticket: "))
        if Gender == "M":
            print("Enter the Age of Male: ")
            age=int(input())
            if age >= 60:
                print(t-30/100*t)
            else:
                print("no discount {t}")
        else:
            print("ticket")
        if Gender == "F":
            print("Enter the Age of Female: ")
            age = int(input())
            if age >= 60:
                print(t-50/100*t)
            if age < 60:
                print(t-30/100*t)
        else:
            ("ticket")
    Railway()'''

# global and local variables (or) scope of the variables
# variable inside and outside the function is called gobal and local variables
# a variable is define above the function and is accessable to the entire global space is called global variable 
# varible inside the function is called local variable
# usage of global key word
# when user want to access the global variable inside the function directly and carry forward the update value even outside the function then we need to use "global" keyword 



# first case of global variable
'''a=4
def check():
    print("inside value is : ",a)
check()
print("outside value is : ",a)'''

# second case of global variable
'''a = 2
def check1():
    a=5
    a=a**2
    print("inside value is: ",a)
check1()
print("outside value is: ",a)'''

# third case of both local and global variables
'''a=6
def check2():
    a=8
    print("inside value is: ",a)
    a=10
    print("updated value is: ",a+5)
    b=13
    b=b+a
    print("value of b is",b)
check2()
print("a value is: ",a)
print("b value is: ",b)''' # this line will give the error coz variable is not declared

# usage of global keyword 
'''a=4
def final():
    global a,b
    print("inside value is : ",a)
    a=15
    print("outside value is : ",a)
    # global b
    b = 20
    b = b+a
    print("Value of b is", b)
final()
print("a value is ", a)
print("b value is ", b)'''

# Attendence Tracker
'''students = int(input("Enter total student: "))
p=0
a=0
for i in range(1,students+1):
    attendence=input(f"student {i} present/absent")
    if attendence =='p':
        p+=1
    elif attendence =='a':
        a+=1
print("...............attendence report...................")  
print("total students",students)
print("number of students present",p)
print("number of students absent"a)'''
