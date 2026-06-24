Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#VARIBLES
print(3+4)
7
#values assigning or data type assigning
a=3
b=4
print(a)
3
print(b)
4
print(a+b)
7
print(a-b)
-1
print(a*b)
12
print(a/b)
0.75
#The varible should start with letters only but it may end with any thing. It should not start with a number
3 = 50
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
3a = 50
SyntaxError: invalid decimal literal
a3 = 50
print(a3)
50
#String assigning
name = "vijitha"
print(name)
vijitha
@ THE STRING MUST BE IN THE QUOTATIONS, WITHOUT QUOTATIONS IT WILL SHOW THE ERROR LIKE THE GIVE BELOW EXAMPLE
SyntaxError: invalid syntax
# THE STRING MUST BE IN THE QUOTATIONS, WITHOUT QUOTATIONS IT WILL SHOW THE ERROR LIKE THE GIVE BELOW EXAMPLE
>>> name = vijitha
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name = vijitha
NameError: name 'vijitha' is not defined
>>> # WHERE WE ARE GIVING THE VARIABLE WE SHOULD GIVE THAT IN THE PRINT ITSELF LIKE IF WE USE CAPITAL LETTER OR SAME THAT SHOULD BE SAME
>>> # CAPITAL_LETTERS => CAPITAL_LETTERS
>>> # SMALL_LETTERS => SMALL_LETTERS
>>> Name = "vijitha"
>>> print(Name)
vijitha
>>> NAME = "vijitha"
>>> print(NAME)
vijitha
>>> # WE SHOULDNOT USE KEYWORDSAS THE VARIABLES
>>> print = "vijitha"
>>> print(print)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(print)
TypeError: 'str' object is not callable
>>> if = 4
SyntaxError: invalid syntax
>>> elif = 3
SyntaxError: invalid syntax
>>> # IT WON'T ALLOW SPECIAL CHARCTER IT ALLOWS ONLY UNDERSCORE(_)
\
>>> @b=3
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> _b=3
>>> print(_b)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(_b)
TypeError: 'str' object is not callable
>>> _=3
>>> print(_)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(_)
TypeError: 'str' object is not callable
