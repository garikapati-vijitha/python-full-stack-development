Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# OPERATORS
# ARTHIMETIC OPERATORS
# HERE THE VARIABLE IS FIXED AND IT DOES NOT CHANGE
A=4
B=2
print(A+B)
6
print(A-B)
2
print(A*B)
8
print(A//B)
2
print(A/B)
2.0
print(A**B)
16
print(A%B)
0

# ASSIGNMENT OPERATORS
# IN ASSIGNMENT NO NEED TO USE PRINT
# THE VARIABLES CHANGE IT WILL TAKE THE UPDATED VALUE
# U CAN TAKE ANY INTEGER
a=4
b=8
print(a+=b)
SyntaxError: invalid syntax
b+=a
b
12
b-=4
b
8
b*=5
b
40
b//=1
b
40
b|=6
b
46
b**=4
b
4477456
b%=6
b
4

#COMPARISION OPERATORS
A=7
B=2
A<B
False
B>A
False
A!=B
True
A>=B
True
A<=B
False
B>=A
False
B
2
B<=A
True
B==A
False
A==B
False
A==8
False
A=2
B
2
B=2
A==B
True

#LOGICAL OPERATORS
a=8
b=9
a<b and b>a
True
a<=b and b>=a
True
a!=b and b==a
False
a<b or b>a
True
a!=b or b==a
True
a<=b or b>=a
True
not True
False
not False
True

# IDENTIFY OPERATORS
>>> a=4
>>> type(a) is int
True
>>> type(a) is not int
False
>>> b = 4.5
>>> type(b) in float
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    type(b) in float
TypeError: argument of type 'type' is not a container or iterable
>>> type(b) is float
True
>>> type(b) is not float
False
>>> c = "vijitha"
>>> type(c) is str
True
>>> type(c) is not str
False
>>> d = 6+5j
>>> type(d) is complex
True
>>> type(d) is not complex
False
>>> e = True
>>> type(e) is bool
True
>>> type(e) is not bool
False
>>> 
>>> # MEMBERSHIP OPERATORS
>>> v = 1,2,3,4,5,6,7,8
>>> 2 in v
True
>>> 36 in v
False
>>> 8 not in v
False
>>> 4657689 not in v
True
