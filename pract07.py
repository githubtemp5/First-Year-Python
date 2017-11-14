###################################
# Alvin Shrestha
# UP826133
###################################


from graphics import *
import math
import random
import time

def getName():
    userInput = input("Enter your name: ")
    while(True):
        userInput = input("Enter your name: ")

def trafficLights():
    win = GraphWin()
    
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    
    while True:
        red.setFill("red")
        amber.setFill("black")
        green.setFill("black")
        time.sleep(2)
        
        red.setFill("red")
        amber.setFill("yellow")
        green.setFill("black")
        time.sleep(2)
        
        red.setFill("black")
        amber.setFill("black")
        green.setFill("green")
        time.sleep(2)
        
        red.setFill("black")
        amber.setFill("yellow")
        green.setFill("black")
        time.sleep(2)
        
def gradeCoursework():
    
    mark = eval(input("Enter a mark: "))
    
    while(calculateGrade(mark)=="X"):
        
        mark = eval(input("Enter a mark: "))
    
        grade = calculateGrade(mark)

    print("The pupil achieved a grade of: ", grade)
    
def orderPrice():
    price = 0
    quantity = 0
    moreQuantity ="yes"
    totalPrice = 0
    while(moreQuantity == "yes"):
        
        price = eval(input("Enter the price of the product in the order: "))
    
        quantity = eval(input("Enter the quantity of the product: "))
        
        totalPrice = totalPrice + price*quantity
        
        moreQuantity = input("Are there any more products in the order?: ")
    print("The total price is £{0:0.2f}".format(totalPrice))
    
def clickableEye():
    win = GraphWin("clickableEye", 600,600)
    
    eyeCentre = Point(300,300)
    eyeRadius = 100
    drawBrownEye(win, eyeCentre, eyeRadius)
    
    clickedOutsideEye = False
    
    label = Text(Point(300,450), "")
    label.draw(win)
    
    while not clickedOutsideEye:
        
        mouse = win.getMouse()
        
        eyePart = getClickedEyePart(mouse, eyeCentre, eyeRadius)
        
        if eyePart == "outside":
            clickedOutsideEye = True
        else:
            label.setText(eyePart)
            
def clickableBoxOfEyes(rows, columns):
    
    windowX = columns * 100 + 100
    windowY = rows * 100 + 100
    
    window = drawWindow(windowX, windowY)
    
    eyeOutside = []
    
    for j in range(100, windowY-50, 100):
        for i in range(100, windowX-50, 100):
            eyeOutside.append(drawEye(window,Point(i, j), 50, "blue"))
            
    
    resultLabel = Text(Point((windowX-25)/2, windowY-25), "")
    resultLabel.draw(window)
    
    
    while(True):
        mouse = window.getMouse()
        insideCircle = False
        for y in range(100, windowY, 100):
            for x in range(100, windowX, 100):
                circle= Point(x,y)
                d = distanceBetweenPoints(mouse, circle)
                clickX = mouse.getX()
                clickY = mouse.getY()
                print(d)
                if(d<=50):
                    resultLabel.setText("Eye at row " + str(round(y/100))+", column "+ str(round(x/100)))
                    insideCircle = True
                    break
                elif(clickX>=50 and clickX<=windowX-50 and clickY>= 50 and clickY <= windowY-50 and not insideCircle):
                    print("HERE")
                    resultLabel.setText("Between eyes")
                elif(clickX<50 or clickX>windowX-50 or clickY<50 or clickY > windowY-50 and not insideCircle):
                    window.close()
                    
def findTheCircle():
    window = GraphWin("Missing Circle")
    
    radius = 30
    
    totalPoints = 0
    
    previousPoint =""
    
    while not radius <=0:
        randX = random.randint(0,200)
        randY = random.randint(0,200)
        
        centre = Point(randX, randY)
        circle = Circle(centre, radius)
        
        for i in range(10):
            mouse = window.getMouse()
            
            d = distanceBetweenPoints(mouse, centre)
        
            if(d<=radius):
                circle.draw(window)
                totalPoints = totalPoints +(10-i)
                print("You Win")
                print("New Game")
                break

            if(i>0):
                prevDistance = distanceBetweenPoints(previousPoint, centre)
                
                if(d > prevDistance):
                    print("Too Far")
                    
                if(d<prevDistance):
                    print("Getting Closer")
                    
            if(i==9):
                print("Game Over")
                print("Total Points",totalPoints)
                radius = 0
                break
                
            previousPoint = mouse
            
        radius = radius- 10 * radius/100
        
def drawWindow(windowX, windowY):
    window = GraphWin("Eyes", windowX, windowY)
    rect = Rectangle(Point(50, windowY-50), Point(windowX-50, 50))
    rect.draw(window)
    return window
    
def temperatureConverter():
    
    print("Type [f] to convert Fahrenheit to Celcius")
    print("Type [c] to convert Celsius to Fahrenheit")
    print("Type [q] to quit")
    
    userInput = input("Select an option: ").lower()
    
    while not(userInput== "q"):
        temp = 0
        if userInput == "f":
            temp = eval(input("Enter the temperature in fahrenheit:"))
            print(temp, "is", fahrenheit2Celsius(temp), "C")
            
        if userInput == "c":
            temp = eval(input("Enter the temperature in celsius:"))
            print(temp, "is", celsius2Fahrenheit(temp), "F")
            
        userInput = input("Select an option: ").lower()
def guessTheNumber():
    randNumber = random.randint(1,100)
    
    for i in range(7):
        guess = eval(input("Guess a number, You have "+ str(7-i) +" tries left. "))
        
        if(guess == randNumber):
            print("You Win!")
            break
        elif (guess > randNumber):
            print("Too High")
        elif (guess<randNumber):
            print("Too Low")
        
        if(i==6):
            print("You Lose!")
            
def tableTennisScorer():
    drawTable()

def drawTable():
    table = GraphWin("Tennis",300,300)
    
    table.setCoords(0,0, 3,3)
    
    border = drawLine(table, Point(1.5,0), Point(1.5, 3))
    
    gameNotWon = True
    
    aPoints = 0
    bPoints = 0
    
    aLabel = drawLabel(table, Point(0.75, 1.5), "A")
    bLabel = drawLabel(table, Point(2.25, 1.5), "B")
    
    while gameNotWon:
        click = table.getMouse()
    
        aPoints, bPoints = updatePoints(click, aPoints, bPoints)
        
        updateLabel(aLabel, aPoints)
        updateLabel(bLabel, bPoints) 
        
        winner = checkWin(aPoints, bPoints)
        
        if(winner=="a"):
            updateLabel(aLabel, str(aPoints)+ "\n You Win!")
            table.getMouse()
            table.close()
        if(winner=="b"):
            updateLabel(bLabel, str(bPoints)+"\n You Win!")
            table.getMouse()
            table.close()
        
def checkWin(ap, bp):
    winner =""
    if(ap>10 and ap>bp):
        if(ap-bp>1):
            winner = "a"
            
    if(bp>10 and bp>ap):
        if(bp-ap>1):
            winner = "b"
    return winner
            
        
def updatePoints(click, ap, bp):
    if(click.getX()<1.5):
        ap+=1
    if(click.getX()>1.5):
        bp+=1
    
    return ap, bp
    
def updateLabel(l, p):
    l.setText(p)
    l.setText(p)
        
def drawLine(win, p1, p2):
    line = Line(p1, p2)
    line.draw(win)
    return line
    
def drawLabel(win, point, text):
    label = Text(point, text)
    label.draw(win)
    return label
    
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32
        
def getClickedEyePart(clickedCoordinates, centreOfEye, radiusOfEye):
    eyePart = ""
    
    distanceFromCentre = distanceBetweenPoints(clickedCoordinates, centreOfEye)
    
    if(distanceFromCentre > radiusOfEye):
        eyePart = "outside"
        
    elif(distanceFromCentre <= radiusOfEye and distanceFromCentre>radiusOfEye/2):
        eyePart = "Sclera"
        
    elif(distanceFromCentre<=radiusOfEye/2 and distanceFromCentre>radiusOfEye/4):
        eyePart = "Iris"
        
    elif(distanceFromCentre<=radiusOfEye/4):
        eyePart = "Pupil"
    
    return eyePart
    
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
    
def drawEye(win, centre, radius, colour):
    
    outside = drawCircle(win, centre, radius, "white")    
    drawCircle(win, centre, radius/2, colour)
    drawCircle(win, centre, radius/4, "black")
    return outside
    
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
    return circle
    
def distanceBetweenPoints(p1,p2):
    
    distance = math.sqrt((p1.getX()-p2.getX())**2 + (p1.getY()-p2.getY())**2)
    
    return distance