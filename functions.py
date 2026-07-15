#functions
#syntax
'''a=10
b=20
print("the sum is: ", a+b)
print("the diff is: ", a-b)
print("the product is: ", a*b)
a=100
b=200
print("the sum is: ", a+b)
print("the diff is: ", a-b)
print("the product is: ", a*b)
a=1000
b=2000
print("the sum is: ", a+b)
print("the diff is: ", a-b)
print("the product is: ", a*b)'''

'''def cal(a,b):
    print("the sum is: ", a+b)
    print("the diff is: ", a-b)
    print("the product is: ", a*b)
cal(10,20)
cal(100,200)
cal(1000,2000)'''

'''def cal(a,b):
    print("the pow is: ", a**b)
    print("the mod is: ", a%b)
    print("the int div is: ", a//b)
cal(5,2)
cal(4,3)
cal(8,2)'''

'''def add(a,b):
    print(a+b)
add(4,6)'''

'''while True:
    def add():
        a=int(input())
        b=int(input())
        print(a+b)
add()'''

'''def add():
    a=int(input("a val"))
    b=int(input("b val"))
    print(a+b)
    add()
add()'''

'''def fulln():
    fn = input("1st name: ")
    ln =input("last name: ")
    print((fn+" "+ln).title())
fulln()'''

#print
'''def mul(a,b):
    print(a*b)
mul(4,6)'''

'''def mul(a,b):
    return a*b
print(mul(7,3))'''

#print v/s return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c,d,e)
cal(2,3)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(2,3))'''

#split bill
'''def bill():
    a=int(input("enter the total mem: "))
    b=int(input("enter the amount: "))
    print("per head bill is: ",b//a)
bill()'''

#.format
'''def bill():
    a=int(input("enter the total mem: "))
    b=int(input("enter the amount: "))
    c=b//a
    print("per head bill is {}".format(c))
    print(f"perhead bill is {c}")
bill()'''

'''def bill():
    a=int(input("enter the total mem: "))
    b=int(input("enter the amount: "))
    c=b//a
    print("per head bill is {}".format(b//a))
    print(f"perhead bill is {b//a}")
bill()
'''


