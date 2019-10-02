def o():
	x=10
	y=20
	def i():
		z=x+y
		print(z)
	return i
a=o()
a()