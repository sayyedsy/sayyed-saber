1.mobile_company_name=['','samsung','lenovo','MI','sony','iphon','nokia']

2.mobile_network_type=('GSM','CDMA','VOLT')
3.mobile_modal_prise={'samsung s8':50000,'nokia k 11':65000,'MI':45000}

4.featur_of_mobile={'samsung':{'RAM':'4GB','ROM':'32GB','CAMERA':'23 MEGA PIXEL'}}

5. mobile_company_name=['','samsung','lenovo','MI','sony','iphon','nokia']
for i in mobile_company_name:
	print(i)
	
6.def dis():
	list1=['samsung','lenovo','MI','sony','iphon','nokia']
	for i in list1:
		if i[0]=='s':
			print(i)
			
7.def display():
	list1=['','samsung','lenovo','MI','sony','iphon','nokia']
	for i in range(1,7):
		print(i,list1[i])

8.mobile_network_type=('','GSM','CDMA','VOLT')
for i in range(1,4):
	print(i,mobile_network_type[i])
	
9.mobile_modal_prise={'samsung s8':50000,'nokia k 11':65000,'MI':45000}
for i in range(0,5):
	print(i,mobile_modal_prise.values()[keys])