import re
code="<html> <head> <title> student website </title> <body> thiboyclass <ul> <li> samsung</li> <li> nokia </li> <li> lenovo </li> </body> </html>"
pattern=re.compile("<li> .* </li>")
match=re.findall(pattern,code)
print(code)
