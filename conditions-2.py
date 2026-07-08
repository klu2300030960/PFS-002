#if else
'''a=15
b=10
if a<b and b>a:
    print("less")
else:
    print("true")'''

'''a=15
b=10
if a<b or b>a:
    print("less")
else:
    print("true")'''

'''a=15
b=10
if not a<b and b>a:
    print("less")
else:
    print("true")'''

#if else condition by using identify operators

'''a = 7
if type(a) is int:
    print("a is None")
else:
    print("a is not None")'''

'''n = "Python"
if type(n) is not int:
    print("yes")
else:
    print("no")'''

#if else conditions by using membership operators

'''a=2,3,4,5,6,7,8,9,10
if 10 in a:
    print("true")
else:
    print("false")

a=2,3,4,5,6,7,8,9,10
if 1 not in a:
    print("true")
else:
    print("false")'''

#if elif else conditions
'''a=8
b=10
if a<b:
    print("less")
elif b>a:
    print("more")
else:
    print("true")'''

'''a=8
b=10
if a==b:
    print("less")
elif b>a:
    print("more")
else:
    print("true")'''

'''a=8
b=10
if a<b:
    print("less")
elif b<a:
    print("more")
else:
    print("true")'''

'''a=8
b=10
if a<b:
    print("less")
elif b<a:
    print("more")
else:
    print("true")'''

'''a=8
b=10
if a is b:
    print("less")
elif b<a:
    print("more")
else:
    print("true")'''

'''a=8
b=10
if b is a:
    print("less")
elif b<a:
    print("more")
else:
    print("true")'''

'''a=8
b=10
if a is not b:
    print("less")
elif b<a:
    print("more")
else:
    print("true")'''

'''a=4
b=9
if a>b and b<=a:
    print("Less")
elif b>a and a<=b:
    print("more")
else:
    print("false")'''

'''a=input("enter the input: ")
if type(a) is int:
    print("It is int")
elif type(a) is str:
    print("it is str")
else:
    print("error")'''

'''a=input()
if type(a) is int:
    print("It is int")
elif type(a) is str:
    print("it is str")
else:
    print("error")'''

#multiple if conditions
'''a=20
b=40
if a<b:
    print("less")
if b>a:
    print("more")
if a!=b:
    print("true")'''

#vote
'''a=int(input())
if a<=18:
    print("not eligible")
if a>18:
    print("eligible to vote")
if a>=50:
    print("Old")'''

'''a=21,56,29,5,0,3
b=int(input())
if a is b:
    print("true")
if a is not b:
    print("false")'''

#nested if
'''a=4
b=6
if a>b:
    print("less")
    if b>a:
        print("more")'''

'''a=4
b=6
if a<b:
    print("less")
    if b>a:
        print("more")
    else:
        print("true")'''

'''a=4
b=6
if a>b:
    print("less")
    if b<a:
        print("more")
else:
    print("false")'''

'''a=4
b=6
if a==b:
    print("less")
    if b<a:
        print("more")
else:
    print("false")'''

'''a=4
b=6
if a<b:
    print("less")
    if b>a:
        print("more")
    else:
        print("true")
else:
    print("false")'''

a=4
b=6
if a<b:
    print("less")
    if b==a:
        print("more")
    elif a>=b:
        print("not equal")
    else:
        print("false")

