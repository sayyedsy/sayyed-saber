import re
src=input("enter what do want to search=")
match=re.fullmatch(src,"i am boss")
print(match)
if match!=None:
    print(" found")
else:
    print(" not found")
    
