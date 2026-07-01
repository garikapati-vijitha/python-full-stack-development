Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#STRING METHOD

#LEN() -> len() is used to tell the length of the string
a = "vijitha"
len(a)
7
a = "garikapati vijitha chowdary"
len(a)
27
c = ""
len(c)
0
d = " "
len(d)
1

# COUNT -> to tell the particular letter or word repeated no. of times will repeat in the string

e = "twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
0
e.count("twinkle")
2
e.count("t")
5
e.count("w")
2
e.count("i")
3
e.count("t")
5

# FINDING A STRING -> 
f = "code"
f.find("o")
1
f.find("e")
3

g = "vijitha"
g.find("v")
0
g.find("i")
1
g.find("a")
6

# ESCAPE SEQUENCE
# \n -> NEW LINE(IT WILL PRINT IN THE LINE)
# \t -> TAB SPACE (SPACE BETWEEN WORDS OR LETTER)
h = "name\n mobile_number\t email_id\n university"
print(h)
name
 mobile_number	 email_id
 university
# NO NEED TO GIVE SPACE BETWEEN THE WORDS AND ESCAPE
h = "name\nmobile_number\temail_id\nuniversity"
print(h)
name
mobile_number	email_id
university
i = "name:vijitha\nmobile_number:1234567890\temail_id:garikapativijithachowdary2004@gmail.com\nuniversity:kl university"
print(i)
name:vijitha
mobile_number:1234567890	email_id:garikapativijithachowdary2004@gmail.com
university:kl university

# REPLACE()
j = "wait until you succeed"
j.replace("wait","work")
'work until you succeed'
k = "wait wait until you succeed"
k.replace("wait","work",1)
'work wait until you succeed'

# upper_case()
l = "vijitha"
l.upper()
'VIJITHA'
# lower_case()
l.lower()
'vijitha'
# capitalize() ->
l.capitalize()
'Vijitha'
l[2].upper()
'J'
m = "garikapati vijitha chowdary"
m.title()
'Garikapati Vijitha Chowdary'

#TRUE OR FALSE CONDITIONS IN STRING
n = "vijitha"
n.isupper()
False
n.islower()
True
n.isdigit()
False
n.isalpha()
True
n.isnum
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    n.isnum
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
n.isnum()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    n.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?

n.isalnum()
True
n.isaldigit()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    n.isaldigit()
AttributeError: 'str' object has no attribute 'isaldigit'. Did you mean: 'isdigit'?
o  = "vijitha@2004"
o.isalnum()
False

p = "vijitha chowdary"
a.startswith("v")
False
a.endswith("y")
True

# STRIP()  (SPACE REMOVE)
# LSTRIP(),RSTRIP()
q="             vijitha                    "
q.strip()
'vijitha'
q.lstrip()
'vijitha                    '
q.rstrip()
'             vijitha'






# SPLIT()
r = "python java c c++"
r.split()
['python', 'java', 'c', 'c++']
s = "vijitha"
s.split()
['vijitha']

# JOIN() -> MERGING GROUP OF WORDS
t = "vja hyd vzg"
"".join(a)
'garikapati vijitha chowdary'

"".join(t)
'vja hyd vzg'
u  = "vja","hyd","vzg"
"".join(u)
'vjahydvzg'
" ".join(u)
'vja hyd vzg'
"v".join(u)
'vjavhydvvzg'

# CONCATENTATION
a = "garikapti"
b = "vijitha"
print(a+b)
garikaptivijitha
fname = "garikapati"
lname = "vijitha"
print(fname+" "+lname)
garikapati vijitha
print((fname+" "+lname).title())
Garikapati Vijitha
'garikapati vijitha chowdary'
'garikapati vijitha chowdary'

# FORMATTING
w = 4
x = 8
print(w+x)
12
print("The Sum is",a+b)
The Sum is garikaptivijitha
print("The Sum is",w+x)
The Sum is 12
x = "vja"
print("The city is", x)
The city is vja

# FORMAT METHOD
y = "motu"
z = "patulu"
print("hello",y+z)
hello motupatulu
print("hello {}{}".format(y,z))
hello motupatulu
print("hello {} {}".format(y,z))
hello motu patulu
>>> print("hello {} hello {}".format(y,z))
hello motu hello patulu
>>> 
>>> # FSTRING
>>> a = "sita"
>>> b = "rama"
>>> print(f"hello {a}{b}")
hello sitarama
>>> print(f"hello {a} {b}")
hello sita rama
>>> print(f"hello {a} hello {b}")
hello sita hello rama
>>> c = "2"
>>> d = "5"
>>> print(c*d)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    print(c*d)
TypeError: can't multiply sequence by non-int of type 'str'
>>> c = 2
>>> d = 5
>>> print(c*d)
10
>>> print(f"product of{c*d}")
product of10
>>> print(f"product of {c*d}")
product of 10
>>> a=2
>>> b=4
>>> c=a*b
>>> print("the product is {}".format(c))
the product is 8
>>> print
<built-in function print>
>>> print(f"product is {c}")
product is 8
>>> print("the product is{}".format(a*b))
the product is8
>>> print(f"the product is {a*b}")
the product is 8
