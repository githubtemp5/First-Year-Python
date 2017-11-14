###################################
# Alvin Shrestha
# UP826133
###################################

from graphics import *

def main():
    doorColour, lightsOn, windowSize, houseNo  = getInputs()
    drawHouse(doorColour, lightsOn, windowSize, houseNo)

def getInputs():
    doorColour = input("Enter door colour: ")
    
    lightsYN = (input("Are the lights on (y/n): ")).lower()
    lightsOn = lightsYN == "y"
    
    windowSize = eval(input("Enter the size of the window: "))
    
    houseNo = input("Enter the house number: ")
    
    return doorColour, lightsOn, windowSize, houseNo

def drawHouse(doorColour, lightsOn, windowDim, houseNo):
    win = GraphWin("House", windowDim, windowDim)
    win.setCoords(0,0,1,1)
    
    #draw roof, wall, door
    drawRoof(win) 
    drawWall(win)
    drawDoor(win, doorColour)

    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawWindow(win, windowColour)
    
    drawHouseNo(win, houseNo)
    
    
def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)

def drawRoof(win):
    roof = Polygon(Point(0.01, 0.70), Point(0.21, 0.99), Point(0.79, 0.99), Point(0.99,0.70))
    roof.setFill("pink")
    roof.draw(win)
    
def drawWall(win):
    wall = drawRectangle(win, Point(0.01,0.70), Point(0.99, 0.01), "brown")
    
def drawDoor(win, doorColour):
    door = drawRectangle(win, Point(0.15, 0.45), Point(0.40, 0.01), doorColour)
    
def drawWindow(win, windowColour):
    window = drawRectangle(win, Point(0.55, 0.45), Point(0.85, 0.15), windowColour)
    
def drawHouseNo(win, houseNo):
    number = Text(Point(0.275,0.35), houseNo)
    number.draw(win)
    
main()
