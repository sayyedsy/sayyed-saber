a=0
b=0
try:

    a=int(input("enter an integer number"))
    b=int(input("enter second integer"))
    print("addition=",a+b)
    print("sustraction=",a-b)
    print("multiplication=",a*b)
    print("division=",a/b)
except ZeroDivisionError:
    print("divisible by zero is not possible")
except ValueError:
    print("please enter valid input")
except NameError:
    print("please enter integer value")
finally:
    print("final; block is execued")
    del a,b
