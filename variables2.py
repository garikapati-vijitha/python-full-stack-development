Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# NO SPECIAL CHARACTERS ARE USED EXPECT UNDERSCORE(_)
_=30
print(_)
30
# NO SPECIAL CHARACTERS ARE USED FOR THE VARIABLES
@=20
SyntaxError: invalid syntax
# BUT WE CAN USE ANY CHARACTERS IN DATATYPE BUT WE CANNOT USE THEM IN THE VARIABLES WE CAN USE THE SPEICAL CHARACTERS IN VARIABLES BUT AFTER THE LETTER BUT NOT AT THE FIRST.
mailid="garikapativijithachowdary2004@gmail.com"
#ASSIGNING THE MULTIPLE VARIBLES IN A LINE
a=9,b=6
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=9;b=6
# THE SYMBOL MUST BE ';'
print(a+b)
15
a,b=9,6
print(a,b)
9 6
a,b,c = 2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a,b,c = 2
TypeError: cannot unpack non-iterable int object
a=b=c=2
print(a+b+c)
6
print(a,b,c)
2 2 2
# THE NUMBER OF VARIABLES MUST BE EQUAL TO THE NUMBER OF DATA TYPES
a,b,c= 2,3,4,5,6,7
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a,b,c= 2,3,4,5,6,7
ValueError: too many values to unpack (expected 3, got 6)
a,b,c=2,3,4
# UNPACKING
 a,b,c=(3,4,5)
 
SyntaxError: unexpected indent
print(a,b,c)
2 3 4
a,b,c=(3,4,5)
print(a,b,c)
3 4 5
>>> # NO SPACE MUST BE GIVEN IN THE VARIABLES USES ONLY UNDERSCORE INSTEAD OF SPACE IN THE VARIABLE, IF A STRING IS ASSIGNNED TO A VARIABLE WE CAN USE THE SPACE IN THE STRING.
>>> first name= vijitha
SyntaxError: invalid syntax
>>> # AND STRING MUST BE IN THE QUOTATIONS IT MAY BE SINGLE OR DOUBLE
>>> first_name = "vijitha"
>>> print(first_name)
vijitha
>>> last_name="garikapati"
>>> print(last_name)
garikapati
>>> print(first_name + " " + last_name)
vijitha garikapati
>>> # FOR SPACE WE NEED TO GIVE EMPTY STRING WITH SINGLE OR DOUBLE OR CAMMA
>>> print(first_name,last_name)
vijitha garikapati
>>> print(first_name+""+last_name)
vijithagarikapati
>>> # CASE SENSITIVE
>>> name="vijitha"
>>> print(name)
vijitha
>>> Name="vijitha"
>>> print(Name)
vijitha
>>> NAME="vijitha"
>>> print(NAME)
vijitha
>>> #DELETION
>>> A=9
>>> print(A)
9
>>> del A
>>> print(A)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(A)
NameError: name 'A' is not defined. Did you mean: 'a'?
