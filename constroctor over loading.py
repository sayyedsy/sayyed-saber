class bank:
    main_balance=500000
    def __init__(self,account_number=None,accouunt_type=None,cash_deposite=None,chek_number=None,chek_amount=None,dd_number=None,dd_amount=None):
        if account_number!=None and accouunt_type!=None and cash_deposite!=None:
            bank.main_balance+=cash_deposite
            print("after cash deposit main balance=",bank.main_balance)
        elif account_number!=None and accouunt_type!=None and chek_number!=None and chek_amount!=None:
            bank.main_balance+=chek_amount
            print("main balance after chek deposit",bank.main_balance)
        elif account_number!=None and accouunt_type!=None and dd_number!=None and dd_amount!=None:
            bank.main_balance+=dd_amount
            print("main balance after dd deposite",bank.main_balance)
        else:
            print("please enter correct information")
b1=bank(account_number=1122334455,accouunt_type="saving",cash_deposite=50000)
b1=bank(account_number=1122334455,accouunt_type="saving",chek_number=543216789,chek_amount=600)
b1=bank(account_number=1122334455,accouunt_type="saving",dd_number=505060,dd_amount=300)
b1=bank(account_number=1122334455,accouunt_type="saving")
