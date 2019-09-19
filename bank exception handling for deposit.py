main_balance=500000
w=0
act=[112233,123456789]
pas=[112233,123456789]
l="yes"
try:
    while l=="yes":
        
        acts=int(input("please enter your account number="))
        pa=int(input("please enter your passwod="))
        while acts in act and pa in pas:
            print("welcom user")
            print("main balance=",main_balance)
            w=int(input("enter wthdraw amount="))
            main_balance=main_balance-w
            print("after deposit main balance=",main_balance)
            break
        else:
            print("pleease enter correct password" "and act no")
        l=input("do you want re login(YES/no)")
        print()
except:
    print("please enter amount in integer")
    
