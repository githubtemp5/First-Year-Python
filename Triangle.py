import math

class Triangle:
    
    def __init__(self, triSide1, triSide2):
        self.side1 = triSide1
        self.side2 = triSide2
        
    def calculateArea(self):
        area = 0.5 * self.side1 * self.side2
        return area
        
    def calculateHypotenuse(self):
        side3 = math.sqrt((self.side1 ** 2) + (self.side2 ** 2))
        return side3
        
    def calculatePerimeter(self):
        perimeter = self.side1 + self.side2 + self.calculateHypotenuse()
        return perimeter
        
        
    def retrieveTriangleInformation(self):
        info = "The triangle with side {0}, {1} with hypotenuse {2} has an area of :{3} and perimeter {4}".format(self.side1, self.side2, self.calculateHypotenuse(), self.calculateArea(), self.calculatePerimeter())
        return info