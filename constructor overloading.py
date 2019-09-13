class construct:
	def __init__(self,a=None,b=None,c=None,d=None):
		if a!=None and b!=None and c!=None and d!=None:
			print("addition of four number",a+b+c+d)
		elif a!=None and b!=None and c!=None:
			print("addition of three number=",a+b+c)
		elif a!=None and b!=None:
			print("addition of two number",a+b)
		else:
			print("enter at least two value")
c1=construct(100,200,600,700)
c1=construct(300,300,400)
c1=construct(500,500)
c1=construct(100)