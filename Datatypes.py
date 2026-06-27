Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
>>> b=5.6
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="code"
>>> type(d)
<class 'str'>
>>> e=5j+6
>>> type(e)
<class 'complex'>
>>> f=j9+7
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    f=j9+7
NameError: name 'j9' is not defined
>>> g=9j
>>> typr(g)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    typr(g)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> type(g)
<class 'complex'>
>>> h=7+9j
>>> type(h)
<class 'complex'>
>>> a=False
>>> type(a)
<class 'bool'>
>>> b=True
>>> type(b)
<class 'bool'>
>>> c"true"
SyntaxError: invalid syntax
>>> c="true"
>>> type(c)
<class 'str'>
