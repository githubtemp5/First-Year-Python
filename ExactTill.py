
class ExactTill:
    def __init__(self, operator, branch):
        self.operator = operator
        self.branch = branch
        self.totalSales = 0
        self.startAmount = 0
        
    def changeOperator(self, newName):
        print("Old Operator: ", self.operator)
        self.operator = newName
        print("New operator name: ", self.operator)
        print("Change Successfull")
    def changeBranch(self, newBranch):
        print("Old Branch Name: ",self.branch)
        self.branch = newBranch
        print("New Branch name: ", self.branch)
        print("Change Successfull")
    def checkTillBalanced(self, amount):
        if amount> self.totalSales:
            print("Not enough amount in the till\nTotal Sales: {0}".format(self.totalSales))
        else:
            print("Enough amount in the till. \nTotal Sales: {0}".format(self.totalSales))
    def makeExactSale(self, amount):
        self.totalSales += amount
        print("Sale Complete")
        print("Total Sales: ", self.totalSales)
    def printTillInformation(self):
        info = "Till Information\nCurrent Operator: {0}\nBranch: {1}\nTotal Sales: £{2}".format(self.operator, self.branch, self.totalSales)
        print(info)
    