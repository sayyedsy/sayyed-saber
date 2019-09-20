a=int(input("enter starting integer="))
b=int(input("enter ending integer="))
while a<b:
	print("table of",a)
	m=1
	while m<10:
		print(a,"×",m,"=",a*m)
		m=m+1
	a=a+1
	