class bank:
	def __init__(self):
		self.main_balance=500000
	def deposit(self,account_no=None,account_type=None,deposit_amount=None,chek_no=None,chek_deposit=None,dd_no=None,dd_amount=None):
		
		if account_no!=None and account_type!=None and deposit_amount!=None:
			self.main_balance=self.main_balance+deposit_amount
			print("main balance after deposit ammount=",self.main_balance)
		elif account_no!=None and account_type!=None and chek_no!=None and chek_deposit!=None:
			self.main_balance=self.main_balance+chek_deposit
			print("after chek deposit main balance",self.main_balance)
		elif account_no!=None and account_type!=None and dd_no!=None and dd_amount!=None:
			self.main_balance=self.main_balance+dd_amount
			print("after deposit main balance =",self.main_balance)
		else:
			print("enter correct data")
b1=bank()


b1.deposit(account_no=1122334455,account_type='saving',deposit_amount=60000)
b1.deposit(account_no=1122334455,account_type='saving',chek_no=54321,chek_deposit=30000)
b1.deposit(account_no=1122334455,account_type='saving',dd_no=112233,dd_amount=20000)