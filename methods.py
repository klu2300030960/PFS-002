Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #extend()
>>> a=["ch", "py", "ml"]
>>> a.append("c")
>>> a,extend(["js", "bs"])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a,extend(["js", "bs"])
NameError: name 'extend' is not defined
>>> a.extend(["js", "bs"])
>>> a
['ch', 'py', 'ml', 'c', 'js', 'bs']
>>> a.append("val")
>>> a.extend(["ka", "da"])
>>> a
['ch', 'py', 'ml', 'c', 'js', 'bs', 'val', 'ka', 'da']
>>> #sort and reverse
>>> a=["ch", "kl
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> a=["ch", "kl", "ab", "jk"]
...    
>>> a.sort()
...    
>>> a
...    
['ab', 'ch', 'jk', 'kl']
>>> a=[90,78,34,80,55,9,7,2,0,5,1]
...    
>>> a.sort()
...    
>>> a
...    
[0, 1, 2, 5, 7, 9, 34, 55, 78, 80, 90]
>>> a.reverse()
...    
>>> a
...    
[90, 80, 78, 55, 34, 9, 7, 5, 2, 1, 0]
