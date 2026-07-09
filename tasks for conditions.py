#vote
'''a=int(input())
if a<=18:
    print("not eligible")
else:
    print("eligible to vote")'''

#even or odd
'''n=int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")'''

#leap yr or not
'''y = int(input("Enter a year: "))
if y % 400 == 0 and y % 4 == 0:
    print(y, "is a Leap Year")
else:
    print(y, "is Not a Leap Year")'''

#guest code
'''n=input()
a = "pooja"
if n == a:
    print("Welcome pooja")
else:
    print("Welcome guest")'''

'''n=input().lower()
if n == "pooja":
    print("Welcome", n)
else:
    print("Welcome Guest")'''

'''l=['chethu','eswar','rupa','nag','akki']
n=input("enter name: ").lower()
if n in l:
    print("welcome",n)
else:
    print("welcome guest")'''

#vowels
'''n=input()
if n in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")'''

'''v=['a','e','i','o','u']
a=input().lower()
if a in v:
    print("Vowel")
else:
    print("Consonant")'''

#social media login

#nested if
'''u=input("username: " )
p=int(input("password: " ))
if u == 'chethana':
    if p == 2106:
        print("Login successful")
else:
    print("Invaid Credentials")'''

#nested if-else
'''u=input("username: " )
p=int(input("password: " ))
if u == 'chethana':
    if p == 2106:
        print("Login successful")
    else:
        print("password incorrect")
else:
    print("Invaid Credentials")'''

#using logical
'''u=input("username: " )
p=int(input("password: " ))
if u == 'chethana' and p == 2106:
    print("Login successful")
else:
    print("Invaid Credentials")'''

#student eligible criteria
#if-else
'''age = int(input("enter your age: "))
marks = int(input("enter your marks: "))
atten = float(input("enter your attendance: "))
if age > 18 and marks > 80 and atten > 70:
    print("You are eligible")
else:
    print("Not eligible")'''

# nested if
'''age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
att = int(input("Enter your attendance: "))
if age >= 18:
    print("Eligible for vote")
    
    if marks >= 80:
        print("Eligible for scholarship")
        
        if att >= 75:
            print("Eligible for exam")
        else:
            print("Not eligible for exam")
    else:
        print("Not eligible for scholarship")
else:
    print("Not eligible for vote")'''

#mam code
'''age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
att = int(input("Enter your attendance: "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")
if marks >= 80:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")    
if att >= 70:
    print("Eligible for exam")
else:
    print("Not eligible for exam")'''

#HOME WORK
#cake price using if-elif-else
'''cake = input("Enter cake name (Red Velvet / Almond / Chocolate): ")

if cake == "Red Velvet":
    print("Price =", 1000)

elif cake == "Almond":
    print("Price =", 800)

elif cake == "Chocolate":
    print("Price =", 1200)

else:
    print("Cake is not available")'''

#using multiple if
'''cake = input("Enter cake name (Red Velvet / Almond / Chocolate): ")

if cake == "Red Velvet":
    print("Price =", 1000)

if cake == "Almond":
    print("Price =", 800)

if cake == "Chocolate":
    print("Price =", 1200)

if cake != "Red Velvet" and cake != "Almond" and cake != "Chocolate":
    print("Cake is not available")'''

#using nested if
'''cake = input("Enter cake name Red Velvet / Almond / Chocolate): ")

if cake == "Red Velvet":
    print("Price =", 1000)
else:
    if cake == "Almond":
        print("Price =", 800)
    else:
        if cake == "Chocolate":
            print("Price =", 1200)
        else:
            print("Cake is not available")'''

#Piza price using if-elif-else
'''item = input("Enter the item name: ")

if item == "BBQ pizza":
    print("Price = 1000")

elif item == "crispy chicken cizza":
    print("Price = 800")

elif item == "paneer pizza":
    print("Price = 600")

elif item == "corn pizza":
    print("Price = 400")

elif item == "french fries & coke":
    print("Price = 200")

else:
    print("Item is not available")'''

#using multiple if

'''item = input("Enter the item name: ")

if item == "BBQ pizza":
    print("Price = 1000")

if item == "crispy chicken cizza":
    print("Price = 800")

if item == "paneer pizza":
    print("Price = 600")

elif item == "corn pizza":
    print("Price = 400")

if item == "french fries & coke":
    print("Price = 200")

if item != "BBQ pizza" and item != "crispy chicken pizza" and item != "paneer pizza" and item != "corn pizza" and item != "french fries & coke":
    print("Item is not available")'''

#using Nested if

'''item = input("Enter the item name: ")

if item == "BBQ Pizza":
    print("Price = 1000")
else:
    if item == "Crispy Chicken Pizza":
        print("Price = 800")
    else:
        if item == "Paneer Pizza":
            print("Price = 600")
        else:
            if item == "Corn Pizza":
                print("Price = 400")
            else:
                if item == "French Fries & Coke":
                    print("Price = 200")
                else:
                    print("Item is not available")'''




