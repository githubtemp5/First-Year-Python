import math
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def calculateArea(self):
        area = self.height * self.width
        return area
    def calculatePerimeter(self):
        perimeter = 2*(self.height + self.width)
        return perimeter
    def calculateDiagonalLength(self):
        diagonalLen = math.sqrt(self.height**2+self.width**2)
        return diagonalLen
        
    def retrieveInformation(self):
        info = "The rectangle with height {0}, width {1} has an area of {2:0.4f} units^2, perimeter {3:0.4f} units and diagonal length of {4:0.4f}".format(self.height, self.width, self.calculateArea(), self.calculatePerimeter(), self.calculateDiagonalLength())
        return info