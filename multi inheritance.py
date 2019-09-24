class costumer:
	def __init__(self):
		self.costumername=input("enter costumer name=")
		self.costumerid=input("enter costumer id=")
	def cdisplay(self):
		print("costumer name=",self.costumername)
		print("costumer id=",self.costumerid)
class bank:		
	def deposit(self):
		depost=int(input("enter deposit amount"))
		mainbalance=500000
		mainbalance=mainbalance+depost
		print("after",mainbalance)
class all(costumer,bank):
	def __init__(self):
		costumer.__init__(self)
		bank.__init__(self)
		print("all cls")
a1=all()
a1.cdisplay()
a1.deposit()	