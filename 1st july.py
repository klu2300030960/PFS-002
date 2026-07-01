Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#concatenation
fn='chethana'
ln='lakshmi'
print(lname+fname)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(lname+fname)
NameError: name 'lname' is not defined
print(ln+fn)
lakshmichethana
print(ln+" "+fn)
lakshmi chethana
print(ln.title()+" "+fn.title())
Lakshmi Chethana
print((ln+" "+fn).title())
Lakshmi Chethana

#formatting
a=3
b=9
print(a+b)
12
print("The answer is:",a+b)
The answer is: 12
c="Hyd"
print("I live in",c)
I live in Hyd

#format method()
a="motu"
b="pathulu"
print("hello {} {}".format(a,b))
hello motu pathulu
print("hello{}{}".format(a,b))
hellomotupathulu
print("hello {} hello {}".format(a,b))
hello motu hello pathulu
print("hello {}{}".format(a,b))
hello motupathulu

#f string()
print(f"hello {a}{b}")
hello motupathulu
print(f"hello {a} {b}")
hello motu pathulu
print(f"hello {a} hello {b}")
hello motu hello pathulu

#format
a=2
b=3
print("answer is {} {}".format(a*b))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print("answer is {} {}".format(a*b))
IndexError: Replacement index 1 out of range for positional args tuple
c=a*b
print("answer is {} {}".format(c))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print("answer is {} {}".format(c))
IndexError: Replacement index 1 out of range for positional args tuple
print("answer is {}".format(c))
answer is 6
#f string
>>> print(f"The answer is {c}")
The answer is 6
>>> print("answer is {}".format(a*b))
answer is 6
>>> print(f"The answer is {a*b}")
The answer is 6
>>> 
>>> #list[]
>>> a=[3.5.6,"pyth",9+7j,True,False]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=[3,5.6,"pyth",9+7j,True,False]
>>> print(a)
[3, 5.6, 'pyth', (9+7j), True, False]
>>> type(a)
<class 'list'>
>>> type('pyth')
<class 'str'>
>>> type(True)
<class 'bool'>
>>> c=9
>>> type[9]
type[9]
>>> type(c)
<class 'int'>
>>> type[c]
type[9]
>>> 
>>> a=['pyh', 'c', 'java']
>>> a.append("c++")
>>> a.append('c++')
>>> print(a.append)
<built-in method append of list object at 0x000001DEAC1193C0>
>>> a.append('c++')
>>> a=["pyh", "c", "java"]
>>> a.append("c++")
>>> 
>>> ##append
>>> a=["ch", "ml", "ka"]
>>> a.append("c")
