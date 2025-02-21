
from abc import ABC ,abstractmethod


#payment strategy

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

#concerete strategy


class Cash(Payment):
    def pay(self):
        print("pay by cash")

class CreditCard(Payment):
    def pay(self):
        print('pay by Credit Card')

class DebitCard(Payment):
    def pay(self):
        print('pay by DebitCard')

#context customer

class Customer:
    def __init__(self, Payment):
        self.Payment=Payment
    def changePaymentMode(self,Payment):
        self.Payment=Payment
    def processPay(self):
        self.Payment.pay()

if __name__=="__main__":
    Cust=Customer(DebitCard()) #intially Customer want to pay with DebitCard
    Cust.processPay()

    #Change the payment mode to Cash
    Cust.changePaymentMode(Cash())
    Cust.processPay()

    #change the payment mode to CrediTCARD
    Cust.changePaymentMode(CreditCard())
    Cust.processPay()
