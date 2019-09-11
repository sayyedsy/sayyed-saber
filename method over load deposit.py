class bank:
	act_bal=0
	def deposit(self,act_number=None,act_typ=None,deposit=None,chekno=None,chekamt=None,ddno=None,ddamt=None):
		if act_number!=None and act_typ!=None and deposit!=None:
			bank.act_bal=bank.act_bal+deposit
			print("after deposit maij balance is",bank.act_bal)
		elif chekno!=None and chekamt!=None and act_number!=None and act_typ!=None:
			bank.act_bal=bank.act_bal+chekamt
			print("after chek amt main bapance is",bank.act_bal)
		elif ddno!=None and ddamt!=None and act_number!=None and act_type!=None:
			bank.act_bal=bank.act_bal+ddamt
			print("after dd add main balance is ",bank.act_bal)
			
b1=bank()
b1.deposit(11223344,"saving",5000)
b1.deposit(33445566,7000,11223344,"saving")
b1.deposit(5588800,700000,11223344,'saving')