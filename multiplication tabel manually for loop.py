print("\t\twelcom to multiplication tabel")
a=int(input("enter starting integer="))
b=int(input("enter ending interger="))
for i in range(a,b+1):
	print("table of",a)
	for j in range(1,11):
		print(i,"×",j,"=",i*j)