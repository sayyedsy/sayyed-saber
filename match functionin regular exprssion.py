import re
srch=input("enter what do you want to seach=")
match=re.match(srch,"india is my country and india is reach in new technology")
if match!=None:
    print("match found")
else:
    print("mathc not found")
