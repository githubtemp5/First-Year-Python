# Practical Worksheet 3: Graphical Programming
# Alvin Shrestha, UP826133

from graphics import *
import math

def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    leftArm=Line(Point(100,100), Point(60,100))
    leftArm.draw(win)
    rightArm=Line(Point(100,100), Point(140,110))
    rightArm.draw(win)
    leftLeg=Line(Point(100,120), Point(60,140))
    leftLeg.draw(win)
    rightLeg=Line(Point(100,120), Point(140,140))
    rightLeg.draw(win)

def drawCircle():
    r=eval(input("Enter the radius of the circle"))
    window=GraphWin("Circle")
    cir=Circle(Point(100,50),r)
    cir.draw(window)
    

def drawArcheryTarget():
    r=10
    win = GraphWin("Archery")
    
    blue=Circle(Point(100,70),r*3)
    blue.setFill("blue")
    blue.setOutline("blue")
    blue.draw(win)

    
    red=Circle(Point(100,70),r*2)
    red.setFill("red")
    red.setOutline("red")
    red.draw(win)
    
    yellow=Circle(Point(100,70),r)
    yellow.setFill("yellow")
    yellow.setOutline("yellow")
    yellow.draw(win)
    
def drawRectangle():
    win=GraphWin("Test Window",200,200)
    
    height=eval(input("Enter the height of the rectangle"))
    width=eval(input("Enter the width of the rectangle"))
    
    rect=Rectangle(Point(100-height/2,100-width/2), Point(100+height/2,100+width/2))
    rect.draw(win)
    
def drawLine():
    win = GraphWin("Line drawer")
    for i in range(10):
        message = Text(Point(100,100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")

def blueCircle():
    win = GraphWin("ClickToDraw")
    p=win.getMouse()
    
    blue=Circle(p,50)
    blue.setOutline("blue")
    blue.draw(win)
    
#def drawLine():
   # win=GraphWin("drawLine")
    
  #  for i in range(10):
      #  x1=eval(input("Enter x1"))
      #  y1=eval(input("Enter y1"))
      #  x2=eval(input("Enter x2"))
      #  y2=eval(input("Enter y2"))
    
     #   line=Line(Point(x1,y1), Point(x2,y2))
    #    line.draw(win)
        
def tenStrings():
    win = GraphWin("ClickForBox", 1000, 1000)
    inputBox = Entry(Point(500,20), 20)
    inputBox.draw(win)
    for i in range(10):
        p=win.getMouse()
        label= Text(p,inputBox.getText())
        label.draw(win)
        inputBox.setText("")
        
def tenColouredRectangle():
    win=GraphWin("TenColouredRect",1000,1000)
    inputColour=Entry(Point(100,20),20)
    inputColour.draw(win)
    
    for i in range(10):
        firstClick=win.getMouse()
        secondClick=win.getMouse()
        
        colouredRect=Rectangle(firstClick,secondClick)
        colouredRect.setFill(inputColour.getText())
        colouredRect.draw(win)
        
        
        
def fiveClickStickFigure():
    win=GraphWin("fiveClickStickFigure",1000,1000)
    circleCentre=win.getMouse()
    x1=circleCentre.getX()
    y1=circleCentre.getY()
        
    circleCircumferencePoint=win.getMouse()
    x2=circleCircumferencePoint.getX()
    y2=circleCircumferencePoint.getY()
    radius=math.sqrt((x2-x1)**2+(y2-y1)**2)
    head=Circle(Point(circleCentre.getX(),circleCentre.getY()),radius)
    head.draw(win)
        
    pointThree=win.getMouse()
    body=Line(Point(x1,y1+radius),Point(pointThree.getX(),pointThree.getY()))
    body.draw(win)
    
    pointFour=win.getMouse()
    arms=Line(Point(pointFour.getX(),pointFour.getY()),Point(x1+(math.sqrt((pointFour.getX()-x1)**2)),pointFour.getY()))
    arms.draw(win)
        
    pointFive=win.getMouse()
    leftLeg=Line(Point(pointThree.getX(),pointThree.getY()),Point(pointFive.getX(),pointFive.getY()))
    leftLeg.draw(win)
    
    rightLeg=Line(Point(pointThree.getX(),pointThree.getY()),Point(pointThree.getX()\
                                                                    +(math.sqrt((pointFive.getX()-pointThree.getX())**2)),pointFive.getY()))
    rightLeg.draw(win)
    

def plotRainfall():
    win=GraphWin("Histogram", 500,600)
    
    diff=20
    
    dayLabelCounter=0;

    yLine=Line(Point(20,20), Point(20,480))     #draw y line
    yLine.draw(win)
    
    xLine=Line(Point(20,480), Point(480,480))       #draw x line
    xLine.draw(win)

    dayLabel=Text(Point(15,497 ),"Day")  #days of rainfall label
    dayLabel.setSize(10) 
    dayLabel.draw(win)  
        
    for counter in range(0,490,70):
        
       xLabel = Text(Point(counter+55,495), dayLabelCounter+1)
       xLabel.draw(win)
       xLabel.setSize(10)
       
       dayLabelCounter=dayLabelCounter+1;
    
    inputBox=Entry(Point(250,550),20)
    inputBox.draw(win)
    
    inputLabel=Text(Point(250,520),"")
    inputLabel.draw(win)
    
    randColour=["red","yellow","blue", "green", "black", "white", "purple"]
    
    for count in range(7):
        
        win.getMouse()
        
        yLabel=Text(Point(10,480-eval(inputBox.getText())),eval(inputBox.getText()))
        yLabel.draw(win)
        yLabel.setSize(10)
        
        rec=Rectangle(Point(diff,480), Point(70+diff, 480-eval(inputBox.getText())))
        rec.draw(win)
        rec.setFill(randColour[count])
        
        diff=diff+70
        inputBox.setText("")
            
        
        
        
        


    
    
    
    
