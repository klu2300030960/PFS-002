Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a = "Chethana"
a[0]+a[1]+a[2]+a[3]+a[4]
'Cheth'
b="Superb"
print(a[0],a[1],a[2],a[3],a[4],a[5])
C h e t h a
print(a[0]a[1]a[2])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b="super"
b[1]+a[2]+b[3]
'uee'
b[0]
's'
b[1]
'u'
b[2]
'p'
b[3]
'e'
b[4]
'r'
c="i am a student"
c[1]+c[2]+c[3]
' am'
>>> a = "simple is better than complex"
>>> a[0]+a[1]+a[2]+a[3]+a[4]a[5]
SyntaxError: invalid syntax
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
>>> a[22]+a[23]+a[24]+a[25]+a[26]+a[27]
'comple'
>>> a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
>>> b = "Codegnan IT Solutions"
>>> b[12]+b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b20]
SyntaxError: unmatched ']'
>>> b[12]+b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'Solutions'
>>> 
>>> #negative
>>> a = "I am learning python"
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
>>> a[-15]+a[-14]+a[13]+a[-12]+a[-11]
'le rn'
>>> a[-18]+a[-17]
'am'
>>> a[-20]
'I'
>>> b="Python FullStack"
>>> b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'Stack'
>>> b[-7]+b[-6]
'll'
>>> b[-8]+b[-7]+b[-6]
'ull'
>>> b[-9]+b[-8]+b[-7]+b[-6]
'Full'
>>> b[-16]+b[-15]+b[-14]+b[-12]+b[11]
'PytoS'
>>> b[-16]+b[-15]+b[-14]+b[-13]+b[-12]+b[11]
'PythoS'
>>> b[-16]+b[-15]+b[-14]+b[-13]+b[-12]+b[-11]
'Python'
>>> b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'Stack'
>>> b[-9]+b[-8]+b[-7]+b[-6]
'Full'
>>> b[-16]+b[-15]+b[-14]+b[-13]+b[-12]+b[-11]
'Python'
