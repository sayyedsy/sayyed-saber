print("1.deposit")
print("2.withdraw")
print("3.Balance Summery")
print("4. Transfer Amount to another account")
print("5.Check your adhar card is linked to your account or not")
print("6.bank details")
print("7.Quit")
class bank:
	def __init__(self):
		self.costumer_name=input("enter costumer name=")
		act=(33955565483,1122334455,123456789)
		costumer_no=int(input("enter costumer account number="))
		print("name is=",self.costumer_name)
		print("account number is=",costumer_no)
		if costumer_no in act:
			print("account is existed")
		else:
			print("account not existed please enter correct account no")
			quit()
		
	def choice(self):
		main_balance=50000
		
		choic=int(input("enter your choice"))
		if choic==1:
			deposit=int(input("enter deposite ammount="))
			main_balance=main_balance+deposit
			print("deposit sucecess after deposit main balance is",main_balance)
		elif choic==2:
			withdraw=int(input("enter withdraw amount="))
			main_balance=main_balance-withdraw
			print("withdraw sucecessfull,after withdraw main balance is",main_balance)
		elif choic==3:
			print("Your Account Balance is",main_balance)
		elif choic==4:
			acounts=(123445,123456)
			
			transfer=int(input("Enter the account number to which you want transfer the money ="))
			if transfer in acounts:
				print("Account is existed ")
				ts=int(input("enter transfer amount  ="))
				main_balance-=ts
				print("Transaction is Successful")
				print("after Transfer main balance is",main_balance)
			else:
				print("You Enter invalid account number !!!")
		elif choic==5:
			adhar=[12345,54321]
			i=int(input("Please Enter your Adhar Card Number ="))
			
			if i in adhar:
				print("Your Adhar card is linked to your Account Number")
			else:
				print("Your Adhar card is not linked to your Account Number")
		elif choic==6:
			print("state bank of india")
			print("adress:ameerpeth hyedrabad")
			print("contact no.:8149366131")
			print("main id:sayyedsaad81@gmail.com")
		elif choic==7:
			quit()
				
			
		else:
			print("wrong choice")
b1=bank()
b1.choice()