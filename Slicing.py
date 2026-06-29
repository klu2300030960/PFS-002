Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="Time is very precious"
a[13:]
'precious'
a[14:21]
'recious'
a[13:21]
'precious'
a[8:]
'very precious'
a[8:13]
'very '
a[0:3]
'Tim'
a[0:4]
'Time'
b="Work until You Succeed"
a[15:]
'ecious'
a[14:]
'recious'
b[15:]
'Succeed'
b[11:14]
'You'
b[0:3]
'Wor'
b[0:4]
'Work'

>>> #negative
>>> c = "vizag is city of Destiny"
>>> c[-15:-12]
'cit'
>>> c[-15:-11]
'city'
>>> c[-7:-1]
'Destin'
>>> c[-7:0]
''
>>> c[-7:-0]
''
>>> c[-7]
'D'
>>> c[-7:]
'Destiny'
>>> c[-24:-20]
'viza'
>>> c[-24:-19]
'vizag'
>>> d="Hi Hello How Are You"
>>> d[-16:-11]
'ello '
>>> d[-17:-11]
'Hello '
>>> d[-10:-8]
'ow'
>>> d[-11:-8]
'How'
>>> d[-8:-5]
' Ar'
>>> d[-7:-4]
'Are'
>>> d[-3:]
'You'
>>> d[-20:-19]
'H'
>>> d[-20:-18]
'Hi'
