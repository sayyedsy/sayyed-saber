class parent:
    def __init__(self,a,b):
        print("addition of two integer=",a+b)
class child(parent):
    def __init__(self,a,b):
        print("multiplication of two number=",a*b)
c1=child(50,60)
