ans="yes"
while ans=="yes":
	try:
		a=int(input("enter first integer="))
		b=int(input("enter enter second integer"))
		print("substraction=",a/b)
	except:
		print("substraction is not possible (zero cannot be dividisible)")
		print("or enter correct integer for division")
	print("addition=",a+b)
	print("substration=",a-b)
	print("multiplication=",a*b)
	print("power=",a**b)
	try:
		print("modulation=",a%b)
		print("floor division=",a//b)
	except:
		print("division of 0 not possible")
		print("or enter integer")
		
	ans=input("do you want repeat(YES/NO)")