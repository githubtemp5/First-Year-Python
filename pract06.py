#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# Alvin Shrestha
# 826133
#-------------------------------------------------------------------------------

from graphics import *
import math
import random

# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

# For exercise 8 
def drawColouredEye(win, centre, radius, colour):
    drawCircle(win, centre, radius, "white")    
    drawCircle(win, centre, radius/2, colour)
    drawCircle(win, centre, radius/4, "black")
    
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
    
def eyePicker():
    
    centreX = eval(getUserInput("Enter the x for the centre: "))
    centreY = eval(getUserInput("Enter the y for the centre: "))
    
    centre = Point(centreX, centreY)
    
    radius = eval(getUserInput("Enter the radius: "))
    
    colour = getUserInput("Enter the colour of the eye: ")
    
    validColour = ["blue", "grey", "green", "brown"]
    
    for i in range(4):
        
        if(colour == validColour[i]):
            win = GraphWin("Window", 400,400)
            drawColouredEye(win, centre, radius, colour)
            break
        else:
            print("Not a valid colour")
            break
            

def drawPatchWindow():
    win = GraphWin("Patch", 100,100)
    
    for counter in range(0,101,10):
        line = Line(Point(counter,0), Point(100-counter,100))
        line.setFill("red")
        line.draw(win)
        
        line2 = Line(Point(100,counter), Point(0,100-counter))
        line2.setFill("red")
        line2.draw(win)
        
def drawPatchWindow0():
    win = GraphWin("F", 100,100)
    
    for x in range(10,101,20):
        colour = ["red","white"]
        colourCounter = 0
        for y in range(10,101,20):
            circle = Circle(Point(x,y),10)
            circle.setFill(colour[colourCounter])
            circle.draw(win)
            colourCounter += 1
            if(colourCounter == 2):
                colourCounter = 0
            
def drawPatchWindow6():
    win = GraphWin("Patch 6", 100,100)
    
    colour = ["white", "red"]
    colourCounter = 0;
    
    for counter in range(0, 101, 10):
        rect = Rectangle(Point(0,100), Point(100-counter, counter))
        rect.setFill(colour[colourCounter])
        rect.draw(win)
        colourCounter+=1
        if(colourCounter==2):
            colourCounter=0
    
def drawPatchWindow9():
    win = GraphWin("Patch 9", 100,100)
    
    rad = 50
    for counter in range(20):
        circle = Circle(Point(50,50+(counter*10)/2),rad)
        circle.setOutline("red")
        circle.draw(win)
        rad-= 5

def drawPatchWindow1():
    win = GraphWin("Patch1", 100,100)
    
    for counter in range(0,101,10):
        rect = Rectangle(Point(counter,100-counter), Point(counter+10, 100-(counter+10)))
        rect.setFill("red")
        rect.setOutline("red")
        rect.draw(win)
        
def drawPatchWindow4():
    win = GraphWin("Patch4", 100, 100)
    
    for counter in (20,81,20):
        line = Line(Point(counter,0), Point(counter,100))
        line.draw(win)
        
def drawPatchWindow2():
    win = GraphWin("Patch 2", 100,100)
    
    for counter in range(0,101,10):
        line = Line(Point(counter-10,0), Point(100,counter+10))
        line.setFill("red")
        line.draw(win)
    
        line2 = Line(Point(0,counter-10), Point(counter+10,100))
        line2.setFill("red")
        line2.draw(win)
    
def drawPatch(win, startX, startY, colour):
    
    xCounter = startX+100
    
    for counter in range(startX, startX+101, 10):
        line = Line(Point(counter,startY), Point((xCounter),startY+100))
        line.setFill(colour)
        line.draw(win)
        xCounter = xCounter-10
    
    yCounter = startY+100
    
    for count in range(startY, startY+101, 10):
        line2 = Line(Point(startX,count), Point(startX+100,(yCounter)))
        line2.setFill(colour)
        line2.draw(win)
        yCounter = yCounter-10
    
def drawPatchwork():
    win = GraphWin("Patches", 300, 200)
    
    for counter in range(0,301,100):
        drawPatch(win, counter, 0, "blue" )
        drawPatch(win, counter, 100, "blue" )
        
def fastFoodOrderPrice():
    price = eval(getUserInput("Enter the price: "))
    
    if(price<10):
        price = price + 1.50
    print("The total price of your order is: £",price)
    
def whatToDoToday():
    temp = eval(getUserInput("Enter today's temperature: "))
    
    activity = getActivity(temp)
    
    print(activity)

        
def getActivity(temp):
    if(temp > 25):
        activity = "You should take a swim in the sea."
    if(temp >=10 and temp <=25):
        activity = "Shopping in Gunwharf Quays is a good idea."
    if(temp < 10):
        activity = "Watching a movie is the best option"
        
    return activity
        
def displaySquareRoots(start, end):
    
    for currentNumber in range(start, end+1):
        print("The square root of {0} is {1:0.3f}".format(currentNumber, getSquareRoot(currentNumber)))
        
def calculateGrade(mark):
    grade=""
    if(mark >=16):
        grade = "A"
    if(mark >=12 and mark<=15):
        grade = "B"
    if(mark >=8 and mark <=11):
        grade = "C"
    if(mark<8):
        grade = "F"
    if(mark<0):
        grade = "X"
    if(mark>20):
        grade = "X"
        
    return grade
    
def eyesAllAround():
    win = GraphWin("EyesAllAround", 500, 500)
    
    colour = ["blue", "grey", "green", "brown"]
    
    colourCounter = 0
    for i in range(30):
        mouse = win.getMouse()
       
        drawColouredEye(win, mouse, 30, colour[colourCounter])
        colourCounter = colourCounter+1
        
        if(colourCounter == 4):
            colourCounter = 0
        
def archeryGame():
    radiusOfBoard=100
    
    centreOfBoard = Point(683, 384)
    
    totalPoints = 0
    
    window=GraphWin("Archery",1366,768)
    
    pointsLabel = Text(Point(1000,100), "")
    pointsLabel.draw(window)
    
    drawArcheryTarget(window, centreOfBoard , radiusOfBoard)
    
    while(True):
    #for i in range(5):
        mouse = window.getMouse()
        
        hitCoordinates = shootArrow(window, mouse)
        
        totalPoints += calculatePoints(hitCoordinates, centreOfBoard, radiusOfBoard)
        pointsLabel.setText("Total Points: "+str(totalPoints))
        
def shootArrow(win, centre):

    centre = randomAtmosphericConditions(centre)
    
    dotOnHit = Circle(centre,3)
    dotOnHit.setFill("white")
    dotOnHit.draw(win)
    
    return centre

def randomAtmosphericConditions(centre):
    
    randX = random.randint(-100,100)
    randY = random.randint(-100,100)
    
    centre = Point(centre.getX()+randX, centre.getY()+randY)
    
    return centre
    
    
def calculatePoints(hitCoordinates, centreOfBoard, radiusOfBoard):
    pointsAchieved= 0
    
    distanceFromCentre = distanceBetweenPoints(hitCoordinates, centreOfBoard)
    
    if(distanceFromCentre > radiusOfBoard*3):
        pointsAchieved = 0
        
    elif(distanceFromCentre <= radiusOfBoard*3 and distanceFromCentre>radiusOfBoard*2):
        pointsAchieved = 2
        
    elif(distanceFromCentre<=radiusOfBoard*2 and distanceFromCentre>radiusOfBoard):
        pointsAchieved = 5
        
    elif(distanceFromCentre<=radiusOfBoard):
        pointsAchieved=10
    
    return pointsAchieved
    
def distanceBetweenPoints(p1,p2):
    
    distance = math.sqrt((p1.getX()-p2.getX())**2 + (p1.getY()-p2.getY())**2)
    
    return distance
    

def drawArcheryTarget(win, centre, r):
    
    blue=Circle(centre, r*3)
    blue.setFill("blue")
    blue.setOutline("blue")
    blue.draw(win)
    
    red=Circle(centre, r*2)
    red.setFill("red")
    red.setOutline("red")
    red.draw(win)
    
    yellow=Circle(centre, r)
    yellow.setFill("yellow")
    yellow.setOutline("yellow")
    yellow.draw(win)
def peasInAPod():
    numberOfPeas = eval(getUserInput("Enter the number of peas to draw: "))
    
    window = GraphWin("Drawing Peas", numberOfPeas*100,100)
    
    for currentNum in range(numberOfPeas):
        peas = Circle(Point(50+currentNum*100, 50), 50)
        peas.setFill("green")
        peas.draw(window)
        
def ticketPrice(distance, age):
    price = 3 + 0.15* int(distance)
    if(age>=60 or age<=15):
        price = price - 40*(price/100)
    
    print("£",price)
    
def numberedSquare(n):
    for counter in range(n,0,-1):
        print("\n")
        for count in range(n):
             print(counter+count, end= " ")
 
def getSquareRoot(number):
    return math.sqrt(number)
    
def getUserInput(text):
    return input(text)