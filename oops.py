# OOPS
# Syntax
# A class contains attribute, variables, object, method, and functions that can manipulate the data.
'''class classname():
    # Attributes
    name = "vijitha"
    age = 21
    place = "vijayawada"
    def fname(method_name):
        print("statements...........")
a.classname()
a.fname()'''

# Class Declaration
'''class Details():
    name = "Vijitha"
    age = 21
    place = "Vijayawada"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
#print(dir(a))
a.display()'''

# Object instantiation(object instant creation)
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
#print(dir(a))
a.data("vijitha",21,"vja")
a.display()
b=Details()
b.data("srujana",21,"vja")
b.display()
c=Details()
c.data("sunitha",21,"vja")
c.display()'''

#Object initilization
# w3school, greeks for greeks
# using __init__
'''class Details():
    #creating a construtor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("jeenith",23,"south Africa")
a.display()'''

'''class Details():
    #creating a construtor
    def __init__(self,name,age,place):
        self.name=input()
        self.age=int(input())
        self.place=input()
    def display(self):
        print(self.name,self.age,self.place)
a=Details("jeenith",23,"south Africa")
a.display()'''

'''class Details():
    name = input("name: ")
    age = int(input("age: "))
    place = input("place: ")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
#print(dir(a))
a.display()'''

'''while True:
    class Details():
        name = input("name: ")
        age = int(input("age: "))
        place = input("place: ")
        def display(self):
            print(self.name,self.age,self.place)
    a=Details()
    #print(dir(a))
    a.display()'''

'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input("name"),int(input("age"),input("place"))
a.display()'''

'''class Details():
    #creating a constructor
    def __init__(self):
        self.name = input()
        self.age = int(input())
        self.place = input()
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.display()'''

# Diff b\w _ (signle underscore) and __()
# when user wants to create a variable with "__" our python interpetor treats it has a special variable to avoid name confits with methods and inner classes
# _ (single underscore)-> public
# __(Double underscore)-> private
'''class employee():
    def __init__(self):
        self.name = "viji"
        self._mailid = "viji@gmail.com"
        self.__salary = 50000 # private variable
a = employee()
#print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._employee__salary)'''


'''class employee():
    def __init__(self):
        self.name = "viji"
        self._mailid = "viji@gmail.com"
        self.__salary = 50000 # private variable
class employee1():
    def __init__(self):
        self.name1 = "sru"
        self._mailid1 = "srui@gmail.com"
        self.__salary1 = 56000
class employee2():
    def __init__(self):
        self.name2 = "suni"
        self._mailid2 = "suni@gmail.com"
        self.__salary2 = 49000
a = employee()
#print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._employee__salary)
b = employee1()
print(b.name1)
print(b._mailid1)
print(b._employee1__salary1)

c = employee2()
print(c.name2)
print(c._mailid2)
print(c._employee2__salary2)'''

# operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(6))
print(a.__mul__(5))
#print(a.__div__(b))
print(a.__pow__(b))
print(a.__ge__(10))
print(a.__le__(6))
print(a.__eq__(b))
a=[2,3,4,5];b=[6,7,8,9]
print(a+b)
print(a.__add__(b))
print(a.__getitem__(2))
print(b.__getitem__(2))
a="code";b="gnan"
print(a+b)
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())
print("srujana".__add__(" "+"p"))'''

# operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(4)
print(x+y)'''

# Method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends")
a = new()
a.sum()
a.sum(2,4,6)
a.sum(6,3)'''

# method overriding
# animals
'''class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def speak(self):
        print("Dog barks")
a = Animal()
b = Dog()
a.speak()
b.speak()'''
        
#vehicles
'''class Vehicles():
    def sound(self):
        print("Vehicles can make sounds")
class Car():
    def sound(self):
        print("Car Horn")
class Bike():
    def sound(self):
        print("Bike Horn")
a = Vehicles()
b = Car()
c = Bike()
a.sound()
b.sound()
c.sound()'''

'''class car():
    def vehical(self):
        print("Thar")
class bike():
    def vehical(self):
        print("Vespa")
a = car()
b = bike()
a.vehical()
b.vehical()'''

# INHERITENCE
# single inheritence
'''class RBI():
    cash = 100000
    def available_cash(cls):
        print("available_cash is",cls.cash)
        print("available_cash is",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash = 50000
    def new_cash(cls):
        print("new_cash is",cls.cash + cls.cash)
        print("new_cash is",cls.cash + RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

# Multiple inheritence
# 1
'''class father():
    def height(self):
        print("height is 5.7 inches")
class mother():
    def weight(self):
        print("weight is 60kgs")
class kid():
    def dob(self):
        print("kid date of birth is may 31")
        
a = father()
b = mother()
c = kid()
a.height()
b.weight()
c.dob()'''

# 2
'''class father():
    def height(self):
        print("height is 5.7 inches")
class mother():
    def weight(self):
        print("weight is 60kgs")
class kid(father, mother):
    def dob(self):
        print("kid date of birth is may 31")
c = kid()
c.height()
c.weight()
c.dob()'''

# multi-level inhertence
'''class grandparents():
    def land(self):
        print("grandparents has a land of 15 acres")
class parents():
    def house(self):
        print("parents has house")
class child(grandparents,parents):
    def car(self):
        print("child has a car")
c = child()
c.land()
c.house()
c.car()'''

# hierarchical inheritence -> it is where one parent class is inhertened by multiple child classes
'''class employee():
    def par(self):
        print("GOOGLE")
class trainer(employee): #child1
    def c1(self):
        print("Trainer Teaches the code")
class Developer(employee): #child2
    def c2(self):
        print("Develops the code")
a=trainer()
b=Developer()
a.par()
a.c1()
b.par()  
b.c2()'''

# Hybrid inheritence -> it means combining more than one type of inheritence
# for eg: hieraarchical + multiple inhertence
'''class person():
    def info(self):
        print("name: jeenith", "age: 23", "Gender: Male")
class trainer(person):
    def teaches(self):
        print("Captain traines the pilot traniees")
class student(person):
    def study(self):
        print("student studies pilot course")
class program_manager(trainer, student):
    def pm(self):
        print("Assigning the classes")
a = program_manager()
a.info()
a.teaches()
a.study()'''

# super()
'''class parent(): #super class
    def __init__(self,name):
        self.name =  name
        print("Parent Construtor")
class child(parent): #sub class
    def __init__(self,name,age):
        self.age = age
        super().__init__(name)
        print("child constructor")
a = child("shobha",46)
#print(dir(a))
print(a.name)
print(a.age)'''

# Encapsulation
# public data
'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj=child()
obj1.method1()
obj1.method2()'''

# _protecteddata()
'''class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

# private data
'''class parent():
    __privatedata="vijitha"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()'''

# abstraction -> hiding unnecessary information from user is called abstraction.
# abstract class -> in abstract class we have one or more abstract methods.
# abstract method -> the method declared without implementation is called abstract method.
# abstraction
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''

'''class A():
    def method1(self):
        print("python")
obj1=A()
obj1.method()'''

'''from abc import ABC,abstractmethod
class A():
    @abstractmethod
    def method1(self):
        print("data")
obj1 = A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
   @abstractmethod
   def method1(self):
       print("codegnan")
obj1 =A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("python course")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("data science")
     def method3(self):
         print("machine learning")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''























