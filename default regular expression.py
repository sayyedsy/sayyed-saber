import re
pattern=re.compile("tcs")
match=pattern.finditer("tcs is company and tcs is software company")
count=0
for i in match:
	count=count+1
print(pattern,"is repetd for",count,"times")