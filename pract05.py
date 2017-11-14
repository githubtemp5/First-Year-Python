#-------------------------------------------------------------------------------
# Practical Worksheet 5: Using functions
# Alvin Shrestha
# UP826133
#-------------------------------------------------------------------------------

from graphics import *
import math

def areaOfCircle(radius):
    return math.pi * radius ** 2

def circumferenceOfCircle(r):
    circumference = 2* math.pi * r
    return circumference

def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawBrownEyeInCentre():
    window = GraphWin("win",200,200)
    
    drawCircle(window, Point(100,100), 60, "white")
    drawCircle(window, Point(100,100), 30, "brown")
    drawCircle(window, Point(100,100), 15, "black")
    
def drawBrownEye(win, centre, radius):
    
    drawCircle(win, centre, radius, "white")    
    drawCircle(win, centre, radius/2, "brown")
    drawCircle(win, centre, radius/4, "black")
    
def drawPairOfBrownEyes():
    win=GraphWin("window")
    drawBrownEye(win,Point(80,80),20)
    drawBrownEye(win,Point(120,80),20)
    
def drawBlockOfStars(width, height):

    for i in range(height):
        print("*" * width)
    
def distanceBetweenPoints(p1,p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    return distance
    
def drawSpaces(width):
        print(" " * width)
        
def drawBlocks(space1,star1,space2,star2,height):
    for i in range(height):
        print(" " * space1, "*" * star1," " * space2, "*" * star2)
        
def drawLetterA():
    drawBlocks(1,8,0,0,2)
    drawBlocks(0,2,5,2,2)
    drawBlocks(0,11,0,0,2)
    drawBlocks(0,2,5,2,3)
    
def drawFourPairsOfBrownEyes():
    win=GraphWin("win",500,500)
    
    for counter in range(4):
        
        mouse1 = win.getMouse()
        mouse2 = win.getMouse()
        
        radius = distanceBetweenPoints(mouse1, mouse2)
        
        drawBrownEye(win, mouse1, radius)
        
def displayTextWithSpaces(text, size, point, win):
    newText= ""
    
    for counter in range(len(text)):
        newText = newText + text[counter] +" "
        
        label = Text(point, newText)
        label.setSize(size)
    
    label.draw(win)
    
def constructVisionChart():
    win=GraphWin("VisionChart", 500,350)

    displayTextWithSpaces(input("Enter the text"), 30, Point(250,50), win)
    displayTextWithSpaces(input("Enter the text"), 25, Point(250,100), win)
    displayTextWithSpaces(input("Enter the text"), 20, Point(250,150), win)
    displayTextWithSpaces(input("Enter the text"), 15, Point(250,200), win)
    displayTextWithSpaces(input("Enter the text"), 10, Point(250,250), win)
    displayTextWithSpaces(input("Enter the text"), 5, Point(250,300), win)
    
def drawStickFigureFamily():
    win= GraphWin("Family Of Sticks", 500, 500)
    
    drawStickFigure(win, Point(50,400), 20)
    drawStickFigure(win, Point(100,360), 30)
    drawStickFigure(win, Point(170,320), 40)
    drawStickFigure(win, Point(260,280), 50)
    

def drawStickFigure(win, head, radius):
    x = head.getX()
    y = head.getY()
    
    head = Circle(head, radius)
    head.draw(win)
    
    arms= Line(Point(x-radius, y+2*radius), Point(x+radius, y+2*radius))
    arms.draw(win)
    
    body = Line(Point(x, y+radius), Point(x, y+radius*3))
    body.draw(win)
    
    leftLeg = Line(Point(x,y+radius*3), Point(x-radius, y+radius*4))
    leftLeg.draw(win)
    
    rightLeg = Line(Point(x, y+radius*3), Point(x+radius, y+radius*4))
    rightLeg.draw(win)

    
    
def drawLetterE():
    for i in [8,2,5,2,8]:
        drawBlockOfStars(i,2)

def circleInfo():
    radius = eval(input("Enter the radius of the circle: "))
    
    area = areaOfCircle(radius)
    circumference = circumferenceOfCircle(radius)
    
    print("The area is {0:0.3f} and the circumference is {1:0.3f}".format(area, circumference))
