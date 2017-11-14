import random

from Dice import Dice
from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle

def main():
    dice = Dice([0,1,2])
    
    result = dice.throwDice()
    
    if result == 0:
        
        r = random.randint(1,10)
        c = Circle(r)
        print(c.retrieveInformation())
        
    elif result ==1:
        side1 = random.randint(1,10)
        side2 = random.randint(1,10)
        rec = Rectangle(side1, side2)
        print(rec.retrieveInformation())
        
    else:
        side1 = random.randint(1,10)
        side2 = random.randint(1,10)
        
        t = Triangle(side1, side2)
        print(t.retrieveTriangleInformation())
        
def totalPrint():
    timesToLoop = eval(input("Enter the number of shapes you want to add"))
    dice = Dice([0,1,2])
    
    totalArea = 0
    totalPerimeter = 0
    
    for i in range(timesToLoop):
        result = dice.throwDice()
        
        if result == 0:
            
            r = random.randint(1,10)
            c = Circle(r)
            
            totalArea += c.calculateArea()
            totalPerimeter += c.calculateCircumference()
            
        elif result == 1:
            side1 = random.randint(1,10)
            side2 = random.randint(1,10)
            rec = Rectangle(side1, side2)
            
            totalArea += rec.calculateArea()
            totalPerimeter += rec.calculatePerimeter()
            
        else:
            side1 = random.randint(1,10)
            side2 = random.randint(1,10)
            
            t = Triangle(side1, side2)
            
            totalArea += rec.calculateArea()
            totalPerimeter += rec.calculatePerimeter()
            
    print("Total Area: ", totalArea)
    print("Total Perimeter: ", totalPerimeter)
        
            
            
            
            
        
        