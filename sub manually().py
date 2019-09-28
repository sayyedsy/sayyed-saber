import re
data="java is powerfull languiage java is opps based languages java is demanded in indusri"
print(data)
find=input("enter which word you want to  find")
print(find)
replace=input("enter replace word =")
string=re.sub(find,replace,data)
print(string)
