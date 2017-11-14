from ExactTill import ExactTill

class ChangeTill(ExactTill):
    def __init__(self, operator, branch, startingAmount):
        ExactTill.__init__(self, operator, branch)
        self.startingAmount = startingAmount
    def makeChangeSale(self, givenAmount, exactSale):
        change = givenAmount - exactSale
        self.makeExactSale(exactSale)
        
        print("Given Amount: ", givenAmount)
        print("Exact Sale:",exactSale)
        print("Change :", change)
        
        
    def changeStartingAmount(self, newAmount):
        print("Old Starting Amount: ", self.startingAmount)
        self.startingAmount = newAmount
        self.totalSales += newAmount
        print("New Starting Amount: ", self.startingAmount)
        