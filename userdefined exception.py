class EnsuficientFundException(Exception):
	def __init__(self,massage):
		self.Errormassage=massage
main_balance=500000
withdraw_amt=int(input("dear costumer please enter withdraw amount="))
if withdraw_amt<main_balance:
	main_balance-=withdraw_amt
	print("after withdraw main balance=",main_balance)
else:
	raise EnsuficientFundException("dear costumer please maintain balance in your account")