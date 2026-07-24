# max(),min(),sum()
#print(max(4,5,7,8,10,20))
#print(min(4,5,7,8,10,20))
#print(sum([4,5,7,8,10,20]))
'''a = 3,4,5,6,7,8,9
print(sum(a))'''

# map()-> each object from a collection and forms a new collection
'''a = [1,2,3,4,5,6,7,8,9,10]
b = [2,4,6,8,10,1,3,5,7,9]
c = list(map(max,a,b))
print(c)
c = list(map(min,a,b))
print(c)'''

"""a = input("data1: ")
b = input("data2: ")
print(a + b)

a,b = input("enter the names: ").split(",")
print(a+b)

a,b = [x for x in input("names: ").split(",")]
print(a+b)

a,b = map(str, input("enter the names: ").split(","))
print(a+b)

a = int(input())
b = int(input())
print(a+b)

a,b = [int(x) for x in input().split(",")] 
print(a+b)

a = int(input()).split(",")
print(a+b) #error

a = map(int,input("enter the values: ").split(","))
print(a+b)

a = list(map(int, input("enter the values: ").split(",")))
print(a+b)
print(type(a))

a = set(map(int,input("enter the value: ").split(",")))
print(a)
print(type(a)

a = tuple(map(int,input("enter the value: ").split(",")))
print(a)
print(type(a))

a = list(map(eval,input("enter the value: ").split(",")))
print(a)
print(type(a))"""

# task
'''a = input("enter the key and value pairs: ")
b = dict(i.split(":") for i in a.split(","))
print(b)'''

# Marks- Analysis Report (mar)

'''students = int(input("Enter the no of students:"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"student {i} marks: "))
    marks.append(mark)
for i in marks:
    print(i)
print("...........Marks Analysis Report............")
print("Total number of students:",students)
print("Highest marks:",max(marks))
print("Lowest marks:",min(marks))
print("Total marks:",sum(marks))
print("Average:",sum(marks)/students)'''




