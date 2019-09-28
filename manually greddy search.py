import re
code=input("enter your program=")
search=input("enter whatto want seach=")
pattern=re.compile(search)
match=re.findall(pattern,code)
print("your find data is=",match)
