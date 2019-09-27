import re
code="<html <head> <title> <body>"
pattern=re.compile("<html>.*<body>")
match=re.findall(pattern,code)
print(match)