#variable length arguments
'''def check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,2.3,4.3)
check1(2,3,4,54.2,2.5,"pooja")'''

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[2,3,4,5,6,7]
check(*b)
c={7,8,9,10}
check(*c)
d={"year":2026,"month":7}
check(*d)'''

'''def check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,2.3,4.3)
check1(2,3,4,54.2,2.5,"pooja",5+9j,True,False)'''

#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names":["harsha","teja","dinesh","sampath"],"marks":[60,70,80],"status":["p","a","p"]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["harsha","teja","dinesh","sampath"],"marks":[60,70,80],"status":["p","a","p"]}
details(**d)'''

#both * and ** usage
'''def final(*a, **b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,2.3,4.3)
final(*data)
d={"names":["harsha","dinesh","teja"],"marks":[60,70,80],"status":["p","a","p"]}
final(**d)
final(*data,**d)'''

#Railway ticket
'''def ticket(age,gender,price):
    if age>60:
        if gender=="male":
            d_price=price*0.7
        else:
            d_price=price*0.5
    else:
        if gender=="male":
            d_price=price
        else:
            d_price=price*0.7
    return d_price
age=int(input("age"))
gender=input("gender")
price=int(input("price"))
print(ticket(age,gender.lower(),price))'''

while True:
    def railway_ticket():
        ticket=1000
        gender=input("enter the gender")
        age=int(input("enter the age"))
        if gender=="m":
            if age>=60:
                print("senior citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                print(ticket)
        elif gender=="f":
            if age>=60:
                print("senior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
    railway_ticket()
              
    
