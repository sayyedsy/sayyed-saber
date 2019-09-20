a=int(input("enter 1st "))
b=int(input("enter 2nd"))
for i in range(a,b+1):
	if i%2==0:
		print(i,"even number")
	else:
		print(i,"odd number")