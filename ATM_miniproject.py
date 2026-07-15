#ATM Application
while True:
    account=100000
    pwd=1234
    card=input("Insert the card: ")
    if card=="c":
        print("Welcome Chethana")
        password=int(input("enter the password: "))
        if password==pwd:
            option=int(input('''choose the option
                                1.balance enq
                                2.withdraw'''))
            if option==1:
                print("your acc bal is",account)
            elif option==2:
                money=int(input("enter the amount: "))
                print(money)
                balance=account-money
                print("rem acc bal is: ",balance)
            else:
                print("invalid option")
        else:
            print("incorrect password")
           
    else:
        print("invalid card")
            
                         
