# GENERATORS
#a generator is also a function which can be used as an iterator(loop) by producing group of vaules,where we can use yield keywords.
# no tuple conperhension in above cases if we remove those brases and keep perantasis then outcome is generator.
# yield vs return
# return can terminate the function where as yield pass the function and go with every successive iteration.
# list_comperhension = [expr for var in collection/range]->
# generator = (i for var in collection/range).
# list comperhension
'''a =[i for i in range(16)]
print(a)
print(type (a))'''

'''a =(i for i in range(16))
print(a)
print(*a)
print(type (a))'''

'''b=list(a)
print(b)'''

# print(tuple(a))
# print(set(a))

# GENERATOR

'''a,b = [int(x) for x in input("enter the values: ").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b = [int(x) for x in input("enter the values: ").split(",")]
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b = [int(x) for x in input("enter the values: ").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
    #return a
print(check(a,b))'''

# return ki yield ki difference

'''def mygen():
    #return "vja"
    #return "hyd"
    #return "vzg"
    return "vja","hyd","vzg"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "c"
print(*mygen())'''

# next()
'''d = mygen()
print(next(d))
print(next(d))
print(next(d))
#print(next(d))'''


















