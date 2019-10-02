def dec(n):
	while n>0:
		yield n
		n=n-1
value=dec(10)
for i in value:
	print(i)