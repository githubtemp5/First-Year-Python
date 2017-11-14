import math
def cookieCutting():
    width=eval(input("Enter the no of cookies along the width."))
    length=eval(input("Enter the no of cookies along the length"))-1
    diameter=eval(input("Enter the diametre of cookie in cm(s)"))
    
    radius=diameter/2
    totalCookies=width*length
    areaOfACookie=math.pi*(radius)**2
    totalMixtureArea=(width*diameter)*(length*diameter)
    completeCookies=totalMixtureArea//areaOfACookie
    totalCookiesArea=completeCookies*areaOfACookie
    
    remainingMixtureArea=totalMixtureArea-totalCookiesArea
    
    
    
    
    print("Radius of each cookie: ", radius, "cm")
    print("Area of each cookie: ", areaOfACookie, "cm^2")
    print("Area of the mixture: ", totalMixtureArea, "cm^2")
    print("Complete cookies", completeCookies)
    print("remaining complete cookies", remainingMixtureArea//areaOfACookie)
   
    
