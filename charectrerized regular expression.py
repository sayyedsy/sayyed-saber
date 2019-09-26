import re
pattern=re.compile("[^a-zA-Z0-9]")
match=pattern.finditer("My name is sayyed saber And my mobile number is 8149366131 and my mail id is sayyedsaad80@gmail.com")
for i in match:
    print(i.start(),"....",i.group())
    
