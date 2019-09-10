class books:
	def __init__(self,racks):
		self.total_racks=racks
	def __add__(self,other):
		return self.total_racks+other.total_racks
rack1=int(input("enter rack1 total book="))
b1=books(rack1)
rack2=int(input("enter rack 2 total book="))
b2=books(rack2)
print("total books in library=",b1+b2)