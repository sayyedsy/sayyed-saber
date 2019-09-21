class bank:
	main_balance=500000
	def deposit(self):
		print("main balance=",bank.main_balance)
		cash=int(input("enter deposit amount="))
		bank.main_balance+=cash
		print("after deposit main balance=",bank.main_balance)
	def withdraw(self):
		withdrw=int(input("enter withdraw amount="))
		if withdrw<=bank.main_balance:
			bank.main_balance-=withdrw
			print("after withdraw main balance =",bank.main_balance)
		else:
			print("please enter below main balance amount")
	def tax(self):
		GST=bank.main_balance*0.04
		print("4% GST")
		print("GST=",GST)
		bank.main_balance-=GST
		print("after GST main balance=",bank.main_balance)
class ICICI(bank):
	def tax(self):
		GST=bank.main_balance*0.08
		print('8% GST')
		print("GST=",GST)
		bank.main_balance-=GST
		print("after GST main balance=",bank.main_balance)
c1=ICICI()
c1.deposit()
c1.withdraw()
c1.tax()