#list comprehension
#a=["codegnan","python","course"]
'''b = str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#syntax for list comprehension
#a=[expr for var var in collections/range]

'''a=[i.upper() for i in a]
print(a)'''

'''a=["vij","hyd","vzg"]
a=[i.title() for i in a]
print(a)'''

'''a=[1,2,3,4,5,6,8,12,13]
a = [i**2 for i in a]
print(a)

a=[1,2,3,4,5,6,8,12,13]
a = [i*i for i in a]
print(a)'''

'''a=[1,2,3,4,5,6,8,12,13]
a = [pow(i,2) for i in a]
print(a)'''

#if-usage in list comprehension
range(16)
#for even
'''a=[i for i in range(16) if i%2==0]
print(a)'''
#for odd
'''a=[i for i in range(16) if i%2!=0]
print(a)'''

'''a=[i for i in range(31)]
print(a)'''

#f=["apple","banana","grapes","kiwi","mango","dragon","berry"]
#a letter fruits
'''f = [i for i in f if 'a' in i]
print(f)
#not a letter fruits
f = [i for i in f if 'a' not in i]
print(f)'''

#no-elif usage in list comprehension
#if-else usage in list comprehension
#range(21)->even num sqares
'''a = [i**2 for i in range(1, 22) if i % 2 == 0]
print(a)
#range(21)->odd num mul 5
a = [i * 5 for i in range(21) if i % 2 != 0]
print(a)'''

'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]

c=[a[i]+b[i] for i in range(len(a))]
print(c)


