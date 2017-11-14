from graphics import *

def footballPlayer():
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(60, 90), Point(140, 90))
    arms.draw(win)
    leg1 = Line(Point(100, 120), Point(70, 170))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(130, 170))
    leg2.draw(win)
    
    ground = Line(Point(0,170),Point(300,170))
    ground.draw(win)
    
    ball = Circle(Point(155,160),10)
    ball.setFill("red")
    ball.draw(win)
    
    goalPost = Rectangle(Point(250,170), Point(260,60))
    goalPost.setFill("blue")
    goalPost.draw(win)
    
    text=""
    label1= Text(Point(200,100),"" )
    label1.draw(win)
    
    for currentCharacter in ['G','o','a','l','!','!','!','!']:
        
        text=text+currentCharacter
        
        mouse=win.getMouse()
        
        label1.setText(text)
        
        ball.move(15,0)
    
    
