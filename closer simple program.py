def outer():
	msg="hello"
	def inner():
		print(msg)
	return inner
a=outer()
a()