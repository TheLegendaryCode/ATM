class Atm:
    def __init__(self,cardNumber,amount,pin):
        self.cardNumber=cardNumber
        self.amount=amount
        self.pin=pin
    def done(self,rupees):
        print("Payment withdraw succesfull - Rupees "+rupees)


cn=input("Please Enter your Card number: ")
am=input("Please Enter the amount: ")
pn=input("Please Enter your pin: ")

a=Atm(cn,am,pn)
a.done(am)
