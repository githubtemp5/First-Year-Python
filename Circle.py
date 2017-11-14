import math

#radius

#area
#circumference
#print information
class Circle:
    def __init__(self, circleRadius):
        self.radius = circleRadius
        
    def calculateArea(self):
        self.area = math.pi * (self.radius**2)
        
        return self.area
    
    def calculateCircumference(self):
        self.circumference = 2 * math.pi * self.radius
        
        return self.circumference
        
    def retrieveInformation(self):
        self.infoString = "A circle of radius {0:2f} \n has an area of {1:0.4f} \n with circumference {2:0.4f}".format(self.radius, self.calculateArea(), self.calculateCircumference())
        
        return self.infoString
                
        
    
        
    
    

        
        
        
        
        
            