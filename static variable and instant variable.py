class company:
	companyid=1011
	company_name="TCS"
	company_adress="hybd"
	def __init__(self):
		self.employee_id=input("enter employee id=")
		self.employee_name=input("employee name =")
		self.employee_salary=int(input("enter emoloyee salary="))
	def company_info():
		print("company id: ",company.companyid)
		print("company name:",company.company_name)
		print("company adress:",company.company_adress)
	def employee_info(self):
		print(self.__dict__)
company.company_info()
c1=company()
c1.employee_info()

		