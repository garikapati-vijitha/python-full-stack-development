# list_comperhension
a=["codegnan","pyhton","course"]
#["codegnan","pyhton","course"]
#pritn(a.upper())

'''b=str(a)
print(b.upper())'''

'''for i in a :
    print(i.upper(),end", ")'''

'''b=[]
for i in a:
    print(i.upper())
print(b)'''

# using list_comprehension
#syntax
#a=[expr for var i in a]

'''a=[i.upper()for i in a]
print(a)'''

# Task

# Task 1
'''a=["vja","hyd","vzg"]
a=[i.title() for i in a]
print(a)'''

# Task 2
# method 1
'''b=[1,2,3,5,6,8,12,13]
b=[i**2 for i in b]
print(b)'''
# method 2
'''b=[i*i for i in b]
print(b)'''
# method 3
'''b=[pow(i,2) for i in b]
print(b)'''

#Task 3

'''a=[i for i in range(16)]
    print(a)''' # numbers for 0 to 15

'''b =[i for i in range(16) if i%2==0]
        print(b)''' # even numbers for 0 to 15

'''b =[for i in range(16) if i%2!=0]
        print(b)''' # odd numbers for 0 to 15

'''b =[i**2 for i in range(21) if i%2==0]
print(b)'''

'''fruits=["apple","banana","mango","grapes","kiwi","drangon","berry"]
fruits=[i for i in fruits if "a" in i]
print(fruits)'''

'''fruits=["apple","banana","mango","grapes","kiwi","drangon","berry"]
fruits=[i for i in fruits if "a" not in i]
print(fruits)'''

# Task 4
# no elif usage in list comprehension
# if else usage

'''no =[i**2 if i%2==0 else i*5 for i in range(31)]
print(no)'''#'''[0, 5, 4, 15, 16, 25, 36, 35, 64, 45, 100, 55, 144, 65,196, 75, 256, 85, 324, 95, 400, 105, 484, 115, 576, 125, 676, 135, 784, 145, 900]

# Task 5
# [6,6,6,6,6]
# method 1
'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

# method 2
'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(5)]
print(c)'''








