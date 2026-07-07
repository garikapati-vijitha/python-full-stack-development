# CONDITIONS
# IF CONDITION BY USING COMPARISION OPERATORS FOR INTEGER
# < ,> , <=, >=, !=, ==
'''a = 10
b = 20
if a < b:
    print("true")'''

'''a = 10
b = 20
if a > b:
    print("true")'''

'''a = 5
b = 7
if a >= b:
    print("true")'''

'''a = 13
b = 54
if a <= b:
    print("true")'''

'''a = 10
b = 20
if a != b:
    print("true")'''

'''a = 20
b = 20
if a == b:
    print("match")'''

# IF CONDITION BY USING COMPARISION OPERATORS FOR INTEGER BY USING RUN TIME INPUT()

'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a<b:
    print("match")'''

'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a>b:
    print("match")'''

'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a>=b:
    print("match")'''

'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a<=b:
    print("match")'''

'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a != b:
    print("match")'''

'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a == b:
    print("match")'''

# IF CONDITION BY USING COMPARISION OPERATORS FOR STRING

'''a = "python"
if a == "python":
    print("match")'''
# run time input
'''a = (input("value of a: "))
b = (input("value of b: "))
if a == b:
    print("match")'''

'''a = "viji"
b = "viji"
if a != b:
    print("match")'''
# run time input
'''a = (input("value of a: "))
b = (input("value of b: "))
if a != b:
    print("match")'''

# if condition by using logical operations(and, or, not) for integer
'''a = 3
b = 6
if a<b and b>a:
    print("true")'''
# run time input
'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a<b and b>a:
    print("true")'''

'''a=4
b=5
if a<=b and b>=a:
    print("true")'''
# run time input
'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a<=b and b>=a:
    print("true")'''

'''a=9
b=12
if a!=b and a == b:
    print("true")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a!=b and a == b:
    print("true")'''

# or 

'''a=2
b=4
if a<b or b>a:
    print("true")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a<b or b>a:
    print("true")'''

'''a=14
b=15
if a<=b or b>=a:
    print("true")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a<=b or b>=a:
    print("true")'''

'''a=3
b=5
if a!=b or a==b:
    print("true")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a!=b or a==b:
    print("true")'''

'''a=5
b=8
if not a<b:
    print("true")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if not a<b:
    print("true")'''

'''a=5
b=8
if not a>b:
    print("true")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if not a>b:
    print("true")'''

"""a=9
b=12
if not a<b and b>a:
    print("true")"""
    
# run time input
'''a=bool(input("value of a: "))
b=bool(input("value of b: "))
if not a<b and b>a:
    print("true")'''
    
"""a=9
b=12
if not a<b or b>a:
    print("true")"""
# run time input
'''a=bool(input("value of a: "))
b=bool(input("value of b: "))
if not a<b or b>a:
    print("true")'''

# if condition by using identify operators(is, is not)

'''a = 4
if type(a) is int:
    print("is is int")'''
# run time input
'''a=int(input("value of a: "))
if type(a) is int:
    print("is is int")'''

'''a = 4
if type(a) is not int:
    print("is is int")'''
# run time input
'''a=int(input("value of a: "))
if type(a) is not int:
    print("is is int")'''

'''a = "vijitha"
if type(a) is str:
    print("is is string")'''
# run time input
'''a=int(input("value of a: "))
if type(a) is str:
    print("is is string")'''

'''a = "vijitha"
if type(a) is not str:
    print("is is string")'''
# run time input
'''a=input("value of a: ")
if type(a) is not str:
    print("is is string")'''

'''a = 4.5
if type(a) is float:
    print("is is float")'''
# run time input
'''a=float(input("value of a: "))
    if type(a) is float:
    print("is is float")'''
    
'''a = 4.5
if type(a) is not float:
    print("is is float")'''
# run time input
'''a=float(input("value of a: "))
if type(a) is not float:
    print("is is float")'''

'''a = 4+5j
if type(a) is complex:
    print("is is complex")'''
# run time input
'''a=comp(input("value of a: "))
if type(a) is complex:
    print("is complex")'''

'''a = True
if type(a) is bool:
    print("is is boolean")'''
# run time input
'''a=bool(input("value of a: "))
if type(a) is bool:
    print("is boolean")'''
    
'''a = True
if type(a) is not bool:
    print("is is boolean")'''
# run time input
'''a=bool(input("value of a: "))
if type(a) is not bool:
    print("is boolean")'''

# if condition by using membership operators
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("True")'''

'''a=2,3,4,5,6,7,8
if 20 not in a:
    print("True")'''

'''a=int(input("a value"))
if 30 in a:
    print("True")''' #error
#run time input
'''a=2,3,4,5,6,7,8
b=int(input("b value: "))
if b in a:
    print("True")'''

'''a=2,3,4,5,6,7,8
b=int(input("b value: "))
if b not in a:
    print("True")'''

# IF ELSE
# if else condition by using comparision operators
'''a=4
b=8
if a<b:
    print("lesser")
else:
    print("greater")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a<b:
    print("lesser")
else:
    print("greater")'''

'''a=4
b=8
if a>b:
    print("lesser")
else:
    print("greater")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a>b:
    print("lesser")
else:
    print("greater")'''

'''a=4
b=8
if a<=b:
    print("lesser")
else:
    print("greater")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a>b:
    print("lesser")
else:
    print("greater")'''

'''a=4


b=8
if a>=b:
    print("lesser")
else:
    print("greater")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a>=b:
    print("lesser")
else:
    print("greater")'''

'''a=4
b=8
if a!=b:
    print("False")
else:
    print("True")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a!=b:
    print("False")
else:
    print("True")'''

'''a=4
b=4
if a==b:
    print("True")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a==b:
    print("True")
else:
    print("False")'''

# if else condition by using logical operations(and, or, not) for integer
'''a = 3
b = 6
if a<b and b>a:
    print("true")
else:
    print("False")'''

# run time input
'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a<b and b>a:
    print("true")
else:
    print("False")'''

'''a=4
b=5
if a<=b and b>=a:
    print("true")
else:
    print("False")'''
# run time input
'''a = int(input("value of a: "))
b = int(input("value of b: "))
if a<=b and b>=a:
    print("true")
else:
    print("False")'''

'''a=9
b=12
if a!=b and a == b:
    print("true")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a!=b and a == b:
    print("true")
else:
    print("False")'''

# or 

'''a=2
b=4
if a<b or b>a:
    print("true")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a<b or b>a:
    print("true")
else:
    print("False")'''

'''a=14
b=15
if a<=b or b>=a:
    print("true")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a<=b or b>=a:
    print("true")
else:
    print("False")'''

'''a=3
b=5
if a!=b or a==b:
    print("true")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if a!=b or a==b:
    print("true")
else:
    print("False")'''

'''a=5
b=8
if not a<b:
    print("true")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if not a<b:
    print("true")
else:
    print("False")'''

'''a=5
b=8
if not a>b:
    print("true")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
b=int(input("value of b: "))
if not a>b:
    print("true")
else:
    print("False")'''

"""a=9
b=12
if not a<b and b>a:
    print("true")
else:
    print("False")"""
    
# run time input
'''a=bool(input("value of a: "))
b=bool(input("value of b: "))
if not a<b and b>a:
    print("true")
else:
    print("False")'''
    
"""a=9
b=12
if not a<b or b>a:
    print("true")
else:
    print("False")"""
# run time input
'''a=bool(input("value of a: "))
b=bool(input("value of b: "))
if not a<b or b>a:
    print("true")
else:
    print("False")'''

# if else condition by using identify operators(is, is not)

'''a = 4
if type(a) is int:
    print("is is int")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
if type(a) is int:
    print("is is int")
else:
    print("False")'''

'''a = 4
if type(a) is not int:
    print("is is int")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
if type(a) is not int:
    print("is is int")
else:
    print("False")'''

'''a = "vijitha"
if type(a) is str:
    print("is is string")
else:
    print("False")'''
# run time input
'''a=int(input("value of a: "))
if type(a) is str:
    print("is is string")
else:
    print("False")'''

'''a = "vijitha"
if type(a) is not str:
    print("is is string")
else:
    print("False")'''
# run time input
'''a=input("value of a: ")
if type(a) is not str:
    print("is is string")
else:
    print("False")'''

'''a = 4.5
if type(a) is float:
    print("is is float")
else:
    print("False")'''
# run time input
'''a=float(input("value of a: "))
    if type(a) is float:
    print("is is float")
else:
    print("False")'''
    
'''a = 4.5
if type(a) is not float:
    print("is is float")
else:
    print("False")'''
# run time input
'''a=float(input("value of a: "))
if type(a) is not float:
    print("is is float")
else:
    print("False")'''

'''a = 4+5j
if type(a) is complex:
    print("is is complex")
else:
    print("False")'''
# run time input
'''a=comp(input("value of a: "))
if type(a) is complex:
    print("is complex")
else:
    print("False")'''

'''a = True
if type(a) is bool:
    print("is is boolean")
else:
    print("False")'''
# run time input
'''a=bool(input("value of a: "))
if type(a) is bool:
    print("is boolean")
else:
    print("False")'''
    
'''a = True
if type(a) is not bool:
    print("is is boolean")
else:
    print("False")'''
# run time input
'''a=bool(input("value of a: "))
if type(a) is not bool:
    print("is boolean")
else:
    print("False")'''

# if else condition by using membership operators
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("True")
else:
    print("False")'''

'''a=2,3,4,5,6,7,8
if 20 not in a:
    print("True")
else:
    print("False")'''

'''a=int(input("a value"))
if 30 in a:
    print("True")
else:
    print("False")''' #error
#run time input
'''a=2,3,4,5,6,7,8
b=int(input("b value: "))
if b in a:
    print("True")
else:
    print("False")'''

'''a=2,3,4,5,6,7,8
b=int(input("b value: "))
if b not in a:
    print("True")
else:
    print("False")'''
