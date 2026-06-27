Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int
int(9)
9
int(9.0)
9
int("pooja")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("pooja")
ValueError: invalid literal for int() with base 10: 'pooja'
int(8+9j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(8+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#float
flat(9)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    flat(9)
NameError: name 'flat' is not defined. Did you mean: 'float'?
float(9)
9.0
float(9.9)
9.9
float("String")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("String")
ValueError: could not convert string to float: 'String'
float(6+9j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

#str
str(5)
'5'
str(9.0)
'9.0'
str("Chethana")
'Chethana'
>>> str(6+9j)
'(6+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> #complex
>>> complex(9)
(9+0j)
>>> complex(9.0)
(9+0j)
>>> complex(9.9)
(9.9+0j)
>>> complex(8j+9)
(9+8j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> #boolen
>>> boolen(9)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    boolen(9)
NameError: name 'boolen' is not defined. Did you mean: 'bool'?
>>> bool(9)
True
>>> bool(9.9)
True
>>> bool("Chethana")
True
>>> bool(7+8j)
True
>>> bool(True)
True
>>> bool(False)
False
