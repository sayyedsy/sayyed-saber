class powerd_device:
	powerd_type=None
	powerd_watts=None
	def prinput():
		powerd_device.powerd_type=input("enter device type")
		
		powerd_device.powerd_watts=input("enter device watts")
	def prinfo():
		print("powerd device type:",powerd_device.powerd_type)
		print("powerd device watts",powerd_device.powerd_type)
class scanner(powerd_device):
	scanner_manifatur_company_name=None
	scanner_id=None
	scanner_modal=None
	scanner_prise=None
	def sinput():
		scanner.scanner_manifatur_company_name=input("enter scanner manifator company name:")
		scanner.scanner_id=input("enter scanner id:")
		scanner.scanner_modal=input("enter scanner modal:")
		scanner.scanner_prise=input("enter scanner prise:")
	def sinfo():
		print("scanner manifator company name",scanner.scanner_manifatur_company_name)
		print("scanner id:",scanner.scanner_id)
		print("scanner modal:",scanner.scanner_modal)
		print("scanner prise:",scanner.scanner_prise)
class printer(powerd_device):
	printer_manifatur_company_name=None
	printer_id=None
	printer_modal=None
	printer_prise=None
	def pinput():
		printer.printer_manifatur_company_name=input("enter printer manifactor company mame")
		printer.printer_id=input("enter printer id:")
		printer.printer_modal=input("enter printer modal:")
		printer.printer_prise=input("enter printer prise:")
	def pinfo():
		print("printer manifator company name",printer.printer_manifatur_company_name)
		print("printer id:",printer.printer_id)
		print("printer modal:",printer.printer_modal)
		print("printer prise:",printer.printer_prise)
class copier(scanner,printer):
	copier_manifatur_company_name=None
	copier_id=None
	copier_modal=None
	copier_prise=None
	def cinput():
		copier.copier_manifatur_company_name=input("enter copier manifactor company mame")
		copier.copier_id=input("enter copier id:")
		copier.copier_modal=input("enter printer modal:")
		copier.copier_prise=input("enter copier prise:")
	def cinfo():
		print("copier manifator company name",copier.copier_manifatur_company_name)
		print("printer id:",copier.copier_id)
		print("printer modal:",copier.copier_modal)
		print("printer prise:",copier.copier_prise)
copier.prinput()
copier.prinfo()
copier.sinput()
copier.sinfo()
copier.pinput()
copier.pinfo()
copier.cinput()
copier.cinfo()