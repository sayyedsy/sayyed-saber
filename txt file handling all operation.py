#write only
"""file1=open("sayyed.txt","w")
file1.write("my name is sayyed saber ")
print("hogya")
file1.close()"""
#userdefine write
"""name=input("enter file name=")
f1=open(name,"w")
data=input("enter any data=")
f1.write(data)
print("hogya")
f1.close()"""
#read only
"""f1=open("SAYYEDSY.txt","r")
data=f1.read()
print(data)"""
#read user define
"""filename=input("enter file name")
f1=open(filename,"r")
data=f1.read()
print(data)
f1.close()"""
#append only
"""file1=open("SAYYEDSY.txt","a")
file1.write("after append my file is adding some conataint")
print("hogya")
file1.close()"""
#append manualy
"""name=input("enter file name=")
file1=open(name,"a")
data=input("enter data=")
file1.write(data)
print("hogya")
file1.close()"""


