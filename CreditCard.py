import random
class CreditCard:
    def __init__(self, cardNumber, nameOnCard, expiryDate, creditLimit):
        self.cardNumber = cardNumber
        self.nameOnCard = nameOnCard
        self.expiryDate = expiryDate
        self.creditLimit = creditLimit
        self.currentBalance = 0
        self.cvv = random.randint(111, 999)
        self.cardVerified = False
        print("Generated CVV: ",self.cvv)
        
    def makePayment(self, amount):
        if self.cardVerified:
            if(amount <= self.currentBalance):
                self.currentBalance -=amount
                print("Current Balance:", self.currentBalance)
            else:
                print("Current Balance:", self.currentBalance)
                print("Not enough funds")
        else:
            print("Verify Card first.")
    def purchaseItem(self, amount):
        if self.cardVerified:
            if(amount <= self.currentBalance):
                self.currentBalance -= amount
                print("Current Balance:", self.currentBalance)
            elif(amount<= self.creditLimit):
                amount -= self.currentBalance
                self.currentBalance = 0
                self.creditLimit -= amount
                print("Current Balance:", self.currentBalance)
                print("Credit Limit:", self.creditLimit)
            else:
                print("Current Balance:", self.currentBalance)
                print("Credit Limit", self.creditLimit)
                print("Not enough funds")
        else:
            print("Verify Card first.")
    def validateCard(self, inputCardNum, inputCVV, inputExpiry):
        if inputCardNum == self.cardNumber and inputCVV == self.cvv and inputExpiry == self.expiryDate:
            self.cardVerified = True
            print("Card Verified.")
        else:
            self.cardVerified = False
            print("Invalid details.")
    def changeCreditLimit(self, newLimit):
        if self.cardVerified:
            print("Limit successfully change from ", self.creditLimit, " to", newLimit)  
            self.creditLimit = newLimit
        else:
            print("Verify Card first.")
    def printAccountInformation(self):
        print("Account Information \nAccount Name: {0}\nCard Number: {1}\nExpiry Date: {2}\nCVV Number: {3}\nCredit Limit:  £{4}\nCurrent Balance: £{5}".format(self.nameOnCard, self.cardNumber, self.expiryDate, self.cvv, self.creditLimit, self.currentBalance))
        
        