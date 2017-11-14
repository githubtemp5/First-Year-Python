import math
class Book:
    def __init__( self , title, author, noPages, isbn, price):
        self.title = title
        self.author = author
        self.noPages = noPages
        self.isbn = isbn
        self.price = price
        self.quantity = 0
    
    def changePrice(self, newPrice):
        self.price = newPrice
        return self.price
        
    def sellCopy(self):
        self.quantity -=1
        return self.quantity
    def restock(self, newCopies):
        self.quantity += newCopies
        return self.quantity
    def retrieveBookInformation(self):
        info = "Title: {0} \nAuthor: {1} \nNumber of Pages: {2} \nISBN: {3} \nPrice: {4} \nQuantity: {5}".format(self.title, self.author, self.noPages, self.isbn, self.price, self.quantity)
        print(info)