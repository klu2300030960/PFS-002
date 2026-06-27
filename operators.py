Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arth
a=2
b=9
print(a+b)
11
print(a-b)
-7
print(a*b)
18
print(a//b)
0
print(a/b)
0.2222222222222222
print(a**b)
512
print(a%b)
2

#assignment
a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
a+b
8
a+=b
a
8
a-=2
a
6
b*=2
b
10
b/=2
b
5.0
b//=2
b
2.0
b**=2
b
4.0
b%=2
b
0.0

#comparision
a=4
b=8
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
A==b
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    A==b
NameError: name 'A' is not defined. Did you mean: 'a'?
a==b
False
a=6
b=6
a==b
True
a<b
False
b>a
False
a!=b
False
False
False

#Logical
a=5
b=7
a<b and a>b
False
a<b and b>a
True
a!=b and a==b
False
a!=b and a==b
False
not True
False
not Falsw
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    not Falsw
NameError: name 'Falsw' is not defined. Did you mean: 'False'?
not False
True

#identify
a=4
type(a) is int
True
type(a) is float
False
type(a) is double
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    type(a) is double
NameError: name 'double' is not defined
type(a) is string
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    type(a) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
tye(a) is str
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    tye(a) is str
NameError: name 'tye' is not defined. Did you mean: 'type'?
type(a) is str
False
a="python"
type is str
False
type(a) is str
True
type(a) is char
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    type(a) is char
NameError: name 'char' is not defined. Did you mean: 'chr'?
type(a) is chr
False

a= 5j+9
type(a) is complex
True
type(a) is int
False
type(a) is float
False
type(a) is bool
False


b=True
type(b) is bool
True
type(b) is str
False
type(b) is int
False

#membership
a=3,8,9,7,4
b
True
8 in a
True
99 not in a
True
4 not in a
False

#bitwise
a=2
b=4
a$b
SyntaxError: invalid syntax
a&b
0
a=5
b=7
a&b
5
bin(2)
'0b10'
bin(4)
'0b100'
bin(5)
'0b101'
bin(7)
'0b111'
bin(8)
'0b1000'

a|b
7
b|a
7
a~b
SyntaxError: invalid syntax
a^b
2
b^a
2
a<<b
640
a>>b
0
0
0

a=2
-(a+1)
-3
~a
-3
a=5
~a
-6
a=9
>>> ~a
-10
>>> b=-11
>>> ~b
10
>>> c=-100
>>> ~c
99
>>> 
>>> a=6
>>> b=9
>>> a^b
15
>>> a=5
>>> b=7
>>> a^b
2
>>> 
>>> 
>>> a=3
>>> a<<2
12
>>> a<<3
24
>>> a=5
>>> a<<3
40
>>> a>>3
0
>>> a>>4
0
>>> a>>1
2
>>> bin(8)
'0b1000'
>>> 8<<2
32
>>> 8>>2
2
