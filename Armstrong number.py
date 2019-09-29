num=int(input("enter any no="))
sum=0
a=num
while num>0:
	dg=num%10
	sum=sum+dg*dg*dg
	num=num//10
if a==sum:
	print("armstrong number")
else:
	print("not armstron")
#407
#153
#1-9