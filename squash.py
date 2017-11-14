#-------------------------------------------------------------------------------
# squash.py - in-class demonstration of program design
# k = move up, m = move down
#-------------------------------------------------------------------------------

from graphics import *

#constants
wallThickness = 0.05
batWidth = 0.15
batX = 0.85
batThickness = 0.05
ballRadius = 0.02

def main():
    court = makeCourt()
    ball = makeBall(court)
    bat = makeBat(court)
    playGame(court, ball, bat)
    
def makeCourt():
    court = GraphWin("Squash", 600, 600)
    court.setBackground("green")
    court.setCoords(0, 0, 1, 1)
    drawRectangle(court, Point(0, 0), Point(1, wallThickness), "orange")
    drawRectangle(court, Point(0, 1), Point(1, 1 - wallThickness), "orange")
    drawRectangle(court, Point(0, wallThickness), Point(wallThickness, 1-wallThickness), "orange")
    return court
    

def makeBall(court):
    ball = drawCircle(court, Point(0.5, 0.5), ballRadius, "white")
    return ball
    
def makeBat(court):
    bat = drawRectangle(court, Point(batX, 0.5-batWidth/2),
                        Point(batX+batThickness, 0.5+batWidth/2), "red")
    return bat

def playGame(court, ball, bat):
    speedX = -0.00004
    speedY = 0.00000
    gameOver = False
    while not gameOver:
        speedX, speedY = checkBallHitWall(ball, speedX, speedY)
        speedX, speedY = checkBallHitBat(ball, bat, speedX, speedY)
        checkMoveBat(court, bat)
        ball.move(speedX, speedY)
        
def checkBallHitWall(ball, speedX, speedY):
    centre = ball.getCenter()
    if centre.getX() - ballRadius <= wallThickness:
        speedX = -speedX
    if centre.getY() + ballRadius >= 1 - wallThickness or \
       centre.getY() - ballRadius <= wallThickness:
        speedY  = -speedY
    return speedX, speedY

def checkBallHitBat(ball, bat, speedX, speedY):
    ballCentre = ball.getCenter()
    ballX = ballCentre.getX() + ballRadius
    ballY = ballCentre.getY()
    topBat = bat.getP2().getY()
    botBat = bat.getP1().getY()
    frontBat = bat.getP1().getX()
    
    if ballX >= frontBat and ballX <= frontBat + speedX and \
      ballY >= botBat and ballY <= topBat:
        speedX = -speedX
        import random
        speedY = random.random() * 0.0001 - 0.00005
    return speedX, speedY
    
def checkMoveBat(court, bat):
    key = court.checkKey()
    if key == "Up":
        bat.move(0, 0.01)
    elif key == "Down":
        bat.move(0, -0.01)

def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)  
    return rectangle  
    
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setOutline(colour)
    circle.draw(win) 
    return circle
    
main()



    
#main()
    
