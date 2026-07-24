#annonymous fun(namesless fun)
'''def cal(x):
    return 2 * x + 5
result = cal(5)
print(result)

def f(x):
    print(2*x+5)
f(5)

def f():
    x=int(input())
    print(2*x+5)
f()
'''
#key word syntax = lambda
'''a=lambda x:2*x+5
print(a(5))'''

#runtime
'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

#task
'''a=int(input())
b=int(input())
c = lambda a,b:a*b
print(c(a,b))'''

'''c= lambda a: a.upper()
print(c("codegnan"))

b="python course"
c=lambda a:a.title()
print(c(b))'''

#fname+lname=fullname
'''a=input()
b=input()
c=lambda a,b:a+b
print(c(a,b))'''

'''a=input()
b=input()
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

'''a,b=[x for x in input("enter the names:").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter()
'''a=[10,20,30,40,50,60,70,80,90]
b=lambda a: [i for i in a if i % 2 == 0]
print(b(a))

b=list(filter(lambda x:x%2 == 0,a))
print(b)

b=list(filter(lambda x:x%2!=0,a))
print(b)'''

#
a=[[],(),{},set(),None,3,5.6,"pooja",4+9j,True,False]
b=list(filter(None,a))
print(b)

