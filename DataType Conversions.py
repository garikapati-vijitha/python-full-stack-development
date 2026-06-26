Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# DATATYPE CONVERSIONS
# INT
int(7)
7
int(4.5)
4
int("vijitha")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("vijitha")
ValueError: invalid literal for int() with base 10: 'vijitha'
int(3+7j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

# FLOAT
float(7)
7.0
float(23.5)
23.5
float("vijitha")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("vijitha")
ValueError: could not convert string to float: 'vijitha'
float(4+6j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(4+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

#STRING
str(4)
'4'
str(2.4)
'2.4'
>>> str("vijitha")
'vijitha'
>>> str(2+78j)
'(2+78j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> # COMPLEX
>>> complex(3)
(3+0j)
>>> KeyboardInterrupt
>>> complex(4.5)
(4.5+0j)
>>> complex("vijitha")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    complex("vijitha")
ValueError: complex() arg is a malformed string
>>> complex(3+5j)
(3+5j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> #boolean
>>> bool(3)
True
>>> bool(0)
False
>>> bool("vijitha")
True
>>> bool(3+56j)
True
>>> bool(True)
True
>>> bool(False)
False
