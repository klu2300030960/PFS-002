Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={2,3,4,5,6,7,8,9}
b={6,7,8,9}
b.issubset(a)
True
a.issubset(b)
False
a.issuperset(b)
True
b.issuperset(a)
False
a=
SyntaxError: invalid syntax
a={3,6.7,"py",8+9j,True,False}
a
{False, True, 3, (8+9j), 6.7, 'py'}
type(a)
<class 'set'>
#union
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#ntersection
a={1,2,3,4,5,6,7,8,9}
b={7,8,9,10,11}
a.intersection(b)
{8, 9, 7}
#difference
a={10,11,12,13,14,15,16}
b={6,7,8,9,12,13,14,15,16,17}
a.difference(b)
{10, 11}
b.differnce(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b.differnce(a)
AttributeError: 'set' object has no attribute 'differnce'. Did you mean: 'difference'?
b.difference(a)
{6, 7, 8, 9, 17}
#symmetric difference
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference(b)
{2, 3, 4, 10, 11}
#update
a={1,2,3,4,5}
b={4,5,6,7,8}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8}
b.update
<built-in method update of set object at 0x00000228A30DA0A0>
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}
a
{1, 2, 3, 4, 5, 6, 7, 8}
#update
a.intersection_update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8}
b.intersection_update(b)
b
{1, 2, 3, 4, 5, 6, 7, 8}
#difference update
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9,10}
a.difference_update(b)
a
{2, 3, 4}
b.difference_update(a)
b
{1, 5, 6, 7, 8, 9, 10}
#symmetricdifference update
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference_update(b)
a
{2, 3, 4, 10, 11}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
#add
a={3,4,5,6,7,8}
a.add(10)
a
{3, 4, 5, 6, 7, 8, 10}
b=a.copy()
b
{3, 4, 5, 6, 7, 8, 10}
a.clear()
a
set()
c=set()
c.add(30)
c
{30}
a={5,6,7,8,9}
a.pop()
5
a.pop(7)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.pop(7)
TypeError: set.pop() takes no arguments (1 given)
a,remove(7)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a,remove(7)
NameError: name 'remove' is not defined
a.remove(7)
a
{6, 8, 9}
a.add(10,11,12)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.add(10,11,12)
TypeError: set.add() takes exactly one argument (3 given)
a.add(10),a.add(11),a.dd(12)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.add(10),a.add(11),a.dd(12)
AttributeError: 'set' object has no attribute 'dd'. Did you mean: 'add'?
a.add(10),a.add(11),a.add(12)
(None, None, None)

#discard
a={2,3,4,5,6)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a={2,3,4,5,6}
a.discard(4)
>>> a
{2, 3, 5, 6}
>>> a.isdisjoint(a)
False
>>> b.isdisjoint(a)
False
>>> a.isdisjoint(b)
False
>>> 
>>> #count
>>> a={4,5,6,7,8}
>>> len(a)
5
>>> a.count(7)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.count(7)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
>>> 
>>> 
>>> #TASKS
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a[3::]
[2, 8, 4, 6, 3, 7, 0]
>>> a[::2]
[9, 5, 8, 6, 7]
>>> a[2:3:5]
[5]
>>> a[1:2:6]
[1]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
