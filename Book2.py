# ============================================================================ #
#
# Book.py
# Class definition for a Book object
#
# V1.1:12.01.17:CAn
#
# ============================================================================ #

class Book:

    def __init__(self, title, author, noPages, isbn, sellingPrice, costPrice):
        self.title = title
        self.author = author
        self.noPages = noPages
        self.isbn = isbn
        self.sellingPrice = sellingPrice
        self.costPrice = costPrice
        self.noCopies = 0

    def changePrice(self, newPrice):
        print("The price is to be updated from {0} to {1}".format(self.sellingPrice, newPrice))
        self.sellingPrice = newPrice

    def sellCopy(self):
        if self.noCopies == 0:
            print("There isn't a copy to sell, restock")
            return 0
        else:
            self.noCopies -= 1
            print("Copy Sold")
            print("You now have {0} copies of {1} by {2}".format(self.noCopies, self.title, self.author))
            return self.sellingPrice

    def restock(self, newCopies):
        self.noCopies += newCopies
        print("You now have {0} copies of {1} by {2}".format(self.noCopies, self.title, self.author))
        return newCopies * self.costPrice

    def retrieveBookInformation(self):
        infoString = "Book Information\nTitle: {0}\nAuthor: {1}\nNumber of Pages: {2}\nISBN: {3}\nCurrent Selling Price: {4}\nCopies in Stock: {5}".format(self.title, self.author, self.noPages, self.isbn, self.sellingPrice, self.noCopies)
        return infoString
