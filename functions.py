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
'''def calculation():
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





































