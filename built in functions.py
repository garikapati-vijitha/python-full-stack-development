# built - in functions
# directory -> collection of files
# ASCII -> chr() , ord()

#print(dir("__builtins__"))
# fromkeys
'''a = "codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))
b = dict.fromkeys(a)
print(b)
c = dict.fromkeys(a,"pooja")
print(c)

c["d"] = "python"
print(c)'''
 
#eval()
'''while True:
    a = int(input("a value: "))
    b = int(input("b value: "))
    print(a+b)'''
    
'''while True:
    a = float(input("a value: "))
    b = float(input("b value: "))
    print(a+b)'''

'''while True:
    a = input("a value: ")
    b = input("b value: ")
    print(a+b)'''

'''while True:
    a = eval(input("a value: "))
    b = eval(input("b value: "))
    print(a+b)'''

# zip() -> zip means we can combined multiple collections into one collection
'''a = [10,20,30,40]
names = ["vijitha","srujana","yashu","sunitha"]
print(a+names)

#b = zip(a,names)
#print(b)

c = list(zip(a,names))
print(c)

c = tuple(zip(a,names))
print(c)

c = dict(zip(a,names))
print(c)

c = set(zip(a,names))
print(c)'''

#enumberate()-> we can give the counter to the collection
names = ["vijitha","srujana","yashu","sunitha"]
'''for i in range(len(names)):
    print(i)'''

#b = list(enumberate(names))
#b = list(enumberate(names,10))
#b = tuple(enumberate(names,100))
#b = dict(enumberate(names,1000))

# ASCII
# chr()
# ord()
'''print(chr(65))
print(chr(90))
print(chr(92))
print(ord("a"))
print(ord("z"))
print(chr("y"))
print(ord(89))'''

'''for i in range(65,91):
    print(chr(i), end = " ")
for i in range(97,123):
    print(chr(i), end = " ")'''


'''for i in range(0, 100):
    print(chr(i), end = " ")'''

'''a = input("enter the name: ")
for i in a:
    print(i, ord(i))'''
