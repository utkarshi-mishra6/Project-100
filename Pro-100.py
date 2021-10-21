class Atm:
    def __init__(self,cardNumber,PinNumber):
        self.PinNumber = PinNumber
        self.cardNumber = cardNumber

       
    def CashWithDrawal(self):
        print("Cash withdrawal")

    def BalanceEnquiry(self):
        print("BankEnquiry")

p = input("Please enter your pin")
c = input("Please enter your card number")
a = Atm(p,c)
a.CashWithDrawal()
a.BalanceEnquiry()

    

    