from graphics import *

def circles():
    win = GraphWin("Circles", 300,300)
    
    for counter in range(10):
        clickedPoint = win.getMouse()
        
        yCoor = clickedPoint.getY()
        circle = Circle(clickedPoint, 15)
        
        if yCoor <100:
            circle.setFill("red")
        elif yCoor >= 100 and yCoor<200:
            circle.setFill("green")
        else:
            circle.setFill("white")
            
        circle.draw(win)
        

def circles2():
    win = GraphWin("Circles2", 300,300)
    
    for yCoor in range(15,301,30):
        for xCoor in range(15,76,30):
            
            clickedPoint = win.getMouse()
            clickedYCoor = clickedPoint.getY()
            
            circle = Circle(Point(xCoor, yCoor), 15)
            
            if clickedYCoor <100:
                circle.setFill("red")
            elif clickedYCoor >= 100 and clickedYCoor<200:
                circle.setFill("green")
            else:
                circle.setFill("white")
            circle.draw(win)
            