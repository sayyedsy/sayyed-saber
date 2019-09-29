class vehical:
	mani_company_name=None
	vehical_modal=None
	vehical_color=None
	vehical_type=None
	vehical_height=None
	def vehical_user_input():
		vehical.mani_company_name=input("enter vehical manifactor company name:")
		vehical.vehical_modal=input("enter vehical modal name")
		vehical.vehical_color=input("enter vehical color:")
		vehical.vehical_type=input("enter vehical type:")
		vehical.vehical_height=input("enter vehical height:")
	def v_info():
		print("vehical company manifator name:",vehical.mani_company_name)
		print("vehical modal name",vehical.vehical_modal)
		print("vehical color:",vehical.vehical_color)
		print("vehical height:",vehical.vehical_height)
		print("vehical type:",vehical.vehical_type)
class register(vehical):
	register_no=None
	register_date=None
	register_place=None
	def register_user_input():
		register.register_no=input("enter registration number:")
		register.register_date=input("enter registration date:")
		register.register_place=input("enter registration place:")
	def r_info():
		print("registration number:",register.register_no)
		print("registration date:",register.register_date)
		print("registration place:",register.register_place)
class car(register):
	def __init__(self):
		self.car_casis_number=input("enter car casis number:")
		self.car_prise=int(input("enter car prise:"))
		self.car_insurance_type=input("enter car insurance type:")
	def prise_calculation(self):
		disk=self.car_prise*0.10
		print("discount is",disk)
		self.car_prise=self.car_prise-disk
		print("after adding discount car prise is",self.car_prise)
		SGST=self.car_prise*0.02
		print("STATE GST IS=",SGST)
		CGST=self.car_prise*0.04
		print("CENTRAL GST IS=",CGST)
		self.car_prise=self.car_prise+SGST+CGST
		print("after add all GST total prise is ",self.car_prise)
	def c_info(self):
		print("car casis number",self.car_casis_number)
		print("car prise:",self.car_prise)
		print("car insurance type",self.car_insurance_type)
car.vehical_user_input()
car.v_info()
car.register_user_input()
car.r_info()
c1=car()
c1.prise_calculation()
c1.c_info()