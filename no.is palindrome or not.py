a=input("enter string=")
b=int(a)
def s (b):
	rev=""
	for i in b:
		rev=i+rev
	print(rev)
	if rev==b:
		print("string is palindrom")
	else:
		print("string is not palindrom")
s(a)