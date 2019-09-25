import re
name=input("enter file name=")
data=input("enter file data=")
file1=open(name,"w")
file1.write(data)
print("file is creted succesfully")
find=input("enter what you want to find in created file=")
pattern=re.compile(find)
match=pattern.finditer(data)
count=0
for i in match:
	count=count+1
print(find,"is repeted for",count,"time")