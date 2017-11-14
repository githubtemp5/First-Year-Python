from Book2 import Book
from Bookshop import Bookshop

def main():
    book = []
    
    daysToModel = eval(input("Days to model: "))
    noOfBooks = eval(input("Enter the number of books: "))
    
    for i in range(noOfBooks):
        
        title = input("Title:")
        author = input("Author: ")
        noPages  = eval(input("Number Pages"))
        isbn = eval(input("ISBN"))
        sellingPrice = eval(input("Selling Price"))
        costPrice = eval(input("Cost Price"))
        
        book.append(Book(title, author, noPages, isbn, sellingPrice, costPrice))
        
        print(book[i])
    bookShop = Bookshop(book)
    bookShop.openBookshop()
    
main()
    
