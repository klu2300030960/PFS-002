#generators
#a=[exp for var in collections/range]
'''a=[i for i in range(21)]
print(a)
print(type(a))
'''

#(exp for var in collections/range)
'''a=(i for i in range(21))
print(a)
print(*a)
print(type(a))
'''

#prin(list(a))
#print(tuple(a))
#print(set(a))

'''a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while  a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while  a<b:
        a=a+1
        return a
print(check(a,b))
'''
#yeild v/s return
'''def mygen():
    return "vij","hyd","vzg"
print(mygen())'''

'''def mygen():
    return "vij","hyd","vzg"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "DSA"
print(*mygen())'''

#next
'''d=mygen()
print(next(d))
print(next(d))
print(next(d))'''

