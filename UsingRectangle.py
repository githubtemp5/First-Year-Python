from Rectangle import *

def main():
    rectangle1 = Rectangle(2,14)
    rectangle2 = Rectangle(28,6)
    
    print("Rectangle 1")
    print()
    print("Object def: ", rectangle1)
    print()
    print("Rectangle side1: ", rectangle1.height)
    print("Rect side2: ", rectangle1.width)
    print()
    print(rectangle1.calculateArea())
    print()
    print(rectangle1.retrieveInformation())
    print()
    print("Object def: ", rectangle2)
    print()
    print(rectangle2.retrieveInformation())

main()
