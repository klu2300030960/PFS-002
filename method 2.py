Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #pop()
>>> a=["black", "white", "blue", "yellow", "pink", "black"]
>>> a.pop()
'black'
>>> a
['black', 'white', 'blue', 'yellow', 'pink']
>>> a.add(6)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.add(6)
AttributeError: 'list' object has no attribute 'add'
>>> a
['black', 'white', 'blue', 'yellow', 'pink']
>>> a.add("black")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.add("black")
AttributeError: 'list' object has no attribute 'add'
>>> a
['black', 'white', 'blue', 'yellow', 'pink']
>>> a.pop(1)
'white'
>>> a
['black', 'blue', 'yellow', 'pink']
>>> #remove
>>> a.remove("blue")
>>> a
['black', 'yellow', 'pink']
>>> #copy
>>> a.copy()
['black', 'yellow', 'pink']
>>> b=a.copy()
>>> b
['black', 'yellow', 'pink']
>>> b.append("green")
>>> b
['black', 'yellow', 'pink', 'green']
a.clear()
a
[]
b
['black', 'yellow', 'pink', 'green']

#len
a=["hi", "hlo", "how"]
len(a)
3
b="hello"
len(b)
5
a.count("o")
0
a.count("hi")
1
b.count("l")
2
