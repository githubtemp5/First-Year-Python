import math

class Borrower:
    def __init__(self, fName, lName, borrowerId, maxAllowed):
        self.fName = fName
        self.lName = lName
        self.borrowerId = borrowerId
        self.maxAllowed = maxAllowed
        self.currentOnLoan = 0
        self.outstandingFine = 0
        
    def increaseMaxLoan(self):
        self.maxAllowed +=1
        return self.maxAllowed
    
    def loanBook(self):
        if self.outstandingFine > 2:
            print("Please pay the outstanding fine first.")
        elif self.currentOnLoan == self.maxAllowed:
            print("Maximum number of loans reached.")
        elif self.currentOnLoan < self.maxAllowed:
            self.currentOnLoan += 1
            print("Loan Successful. No. of books currently on loan: ", self.currentOnLoan)
            
    def returnBook(self):
        if self.outstandingFine > 2:
            print("Please pay the outstanding fine first.")
        elif self.currentOnLoan < 1:
            print("No books on loan.")
        else:
            self.currentOnLoan -= 1
            print("Book returned. No. of books currently on loan: ", self.currentOnLoan)
            
    def payFine(self):
        if self.outstandingFine < 1:
            print("No fine to be paid.")
        else:
            self.outstandingFine -= 1
            print("Fine Paid. No of fines remaining: ", self.outstandingFine)
        
    def retrieveInformation(self):
        info = "Full Name: {0} {1}\nBorrowerID: {2}\nMaximum Allowed: {3}\nCurrent loan(s): {4}\nOutstanding Fine: {5}".format(self.fName, self.lName, self.borrowerId, self.maxAllowed, self.currentOnLoan, self.outstandingFine)
        
        print(info)
        