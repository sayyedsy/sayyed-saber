prise=int(input("enter your prise="))
GST=prise*0.05
print("GST is=",GST)
CGST=prise*0.07
print("CGST is=",CGST)
prise=prise+GST+CGST
print("after add GST prise is=",prise)