#key word and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="pooja"
    mailid="p@.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id="10",name="bhanu",mailid="b@gmail.com")
Details(id="20",name="nayana",mailid="n@gmail.com")
Details(30,"chethana","c@gmail.com")
Details("h@gmail.com",40,"harika")
Details(mailid="r@gmail.com",name="rupa",id="50")'''

#default arguments
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''

'''def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''

'''def Grocery(price,item="ghee"):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''

#cake_name,price,quantity
'''def Grocery(cakename,price,quan):
    print("cakename is %s" %cakename)
    print("price is %.2f" %price)
    print("quan %d" %quan)
Grocery("blackforest",1200,1)'''

#* argument(* is used to unpack the elements)
'''a=[10,20,30,40,50]
print(a)
print(*a)'''

'''b=(5,6,7,8,9,10)
print(b)
print(*b)'''

'''c={6,7,8,9}
print(c)
print(*c)'''

'''d={"name":"pooja","year":2026,"month":6}
print(d)
print(*d)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,9
print(a)
print(b)
print(c)'''

'''a,b,c=3,4,5
print(a)
print(b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(*c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c) error'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''
