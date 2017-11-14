from CreditCard import CreditCard

class ContactlessCard(CreditCard):
    def __init__(self, cardNumber, nameOnCard, expiryDate, creditLimit, individualLimit):
        CreditCard.__init__(self, cardNumber, nameOnCard, expiryDate, creditLimit)
        self.contactless = False
        self.individualLimit = individualLimit
        
    def disableContactless(self):
        if self.contactless:
            self.contactless = False
            print("Contactless disabled")
        else:
            print("Contactless already disabled")
    def enableContactless(self):
        if self.contactless:
            print("Contactless already enabled.")
        else:
            self.contactless = True
            print("Contactless now enabled.")
    def makePayment(self, amount):
        if self.cardVerified:
            if(amount<=self.currentBalance):
                if(amount<=self.individualLimit):
                    self.currentBalance -= amount
                    print("Current Balance:", self.currentBalance)
                else:
                    print("Amount exceeds individual limit")
            else:
                print("Not enough funds.")
        else:
            print("Verify Card first.")
        