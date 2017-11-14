######################################################################################################################################
# Alvin Shrestha                                                                                                                     #
# UP826133                                                                                                                           #
######################################################################################################################################

from graphics import *

# radius of the circles
radius = 10

#background colour of the window
bgColour = "white"





def main():
    
     patchDimension, colours = getInputs()
     
     window = createWindow(patchDimension)
     
     drawPatches(window, patchDimension, colours)
     
def getInputs():
    
    #defining valid colours and dimensions                      
    validColour = ["red", "green", "blue", "orange", "brown", "pink"]
    validDimensions = ["5","7","9"]
    
    inputPatchDimension =""
    inputColour = ""
    colours = []
    
    inputPatchDimension = input("Enter the size of the pattern: ")
    
    #loop to enter dimension until it is valid.
    while inputPatchDimension not in validDimensions or not inputPatchDimension.isdigit():
        
        print("Invalid size, only 5, 7 or 9 allowed")
        
        inputPatchDimension = input("Enter the size of the pattern: ")
    
    #calculating the size of the window
    inputPatchDimension = eval(inputPatchDimension) *100
    
    #loop for getting three valid colours
    for counter in range(3):
        inputColour =""
        inputColour = (input("Enter a colour: ")).lower()
        
        while(inputColour not in validColour or inputColour in colours):
            
            print("Invalid colour or colour already entered. Valid colours: ", validColour)
            
            inputColour = (input("Enter a colour: ")).lower()
        
        colours.append(inputColour)
        
    return inputPatchDimension, colours
    
def drawPatches(win, patchDimension, colours):
    
    patchII = []
    patchIIColour = []
    patchIIStartPoints = []
    
    patchIFill = []
    patchIColour = []
    patchIOutline = []
    patchIStartPoints = []
    
    patchIICoor = []
    
    counter = int(patchDimension/100)-1
    
    #defining intial colours
    colourForCurrentRow = []
    
    for counter in range(int(patchDimension/100)):
        colourForCurrentRow.append(0)
        
    currentColumn = int(patchDimension/100) -1
    
    #drawing the patch itself. The patch is drawn by rows from left to right. Depending on where the current point is either patch I or II is selected.
    for y in range(0, patchDimension, 100):
        
        patchIICoor.append(counter)
        
        # selects colours to be drawn for the current row. Stores them in colourForCurrentRow.
        for change in range(currentColumn, int(patchDimension/100), 1):
            
            if(change == currentColumn):
                colourForCurrentRow[change] = 1
            else:
                colourForCurrentRow[change] =  2
                
        currentColumn -=1
            
        if(int(y/100)%2 == 1):
            counter -= 2
        
        for x in range(0, patchDimension, 100):
            
            if(int(x/100) in patchIICoor):
                patchII.append(drawPatchII(win, colours[colourForCurrentRow[int(x/100)]], x, y)) 
                patchIIColour.append(colourForCurrentRow[int(x/100)])
                patchIIStartPoints.append(Point(x, y))
                
            else:
                tempPatchIFill, tempPatchIOutline = drawPatchI(win, colours[colourForCurrentRow[int(x/100)]], x, y)
                patchIFill.append(tempPatchIFill)
                patchIOutline.append(tempPatchIOutline)
                patchIColour.append(colourForCurrentRow[int(x/100)])
                patchIStartPoints.append(Point(x,y))
                
    while(True):
        clickedPoint = win.getMouse()
        
        clickedStartX = correctBoundary(int(clickedPoint.getX()/100)*100, patchDimension)
        clickedStartY = correctBoundary(int(clickedPoint.getY()/100)*100, patchDimension)
        
        clickedPatch, clickedPatchIndex = identifyPatch(clickedStartX, clickedStartY, patchIStartPoints, patchIIStartPoints)
        
        if(clickedPatch == "patchI"):
            nextColour = calculateNextColour(patchIColour[clickedPatchIndex])
            for i in patchIOutline[clickedPatchIndex]:
                i.setOutline(colours[nextColour])
            for j in patchIFill[clickedPatchIndex]:
                j.setFill(colours[nextColour])
            patchIColour[clickedPatchIndex] = nextColour
            
        else:
            nextColour = calculateNextColour(patchIIColour[clickedPatchIndex])
            
            for i in patchII[clickedPatchIndex]:
                i.setFill(colours[nextColour])
            patchIIColour[clickedPatchIndex] = nextColour
         

def calculateNextColour(currentCol):
    nextCol =0
    if currentCol == 2:
        nextColour = 0
    else:
        nextColour = currentCol + 1
    return nextColour
        
def identifyPatch(xCoor, yCoor, patchIStartPoints, patchIIStartPoints):
    for current in patchIStartPoints:
        if(current.getX() == xCoor and current.getY() == yCoor):
            return "patchI", patchIStartPoints.index(current)
            break
            
    for current in patchIIStartPoints:
        if(current.getX() == xCoor and current.getY() == yCoor):
            return "patchII", patchIIStartPoints.index(current)
            break

        
      
      
def correctBoundary(point, patchDimension):
    if(point == patchDimension):
        point = patchDimension-100
    return point
    
def drawPatchI(win, colour,  startPointX, startPointY):
    
    fillCircles = []
    outlineCircles = []
    
    # draws Vertical half circles
    for i in range(startPointX+radius, startPointX+radius*10, radius*4):
        for j in range(startPointY+radius, startPointY+radius*10, radius*2):
            
            centre = Point(i, j)
            
            circle = drawCircle(win, centre, radius, colour) 
            fillCircles.append(circle)          
            
            # calculating points for the rectangle to block one half of the circle.
            p1 = Point(i, j+radius)
            p2 = Point(i-radius, j-radius)
            
            rect = drawRectangle(win, p1, p2)
            
            outlineCircle = drawOutlineCircle(win, centre, radius, colour)
            outlineCircles.append(outlineCircle)


    # draws Horizontal half circles
    for i in range(startPointX+radius*3, startPointX+radius*10, radius*4):
        for j in range(startPointY+radius, startPointY+radius*10, radius*2):

            centre = Point(i, j)
            
            circle = drawCircle(win, centre, radius, colour)
            fillCircles.append(circle)  
            
            p1 = Point(i-radius, j)
            p2 = Point(i+radius, j+radius)
            
            rect = drawRectangle(win, p1, p2)
        
            outlineCircle = drawOutlineCircle(win, centre, radius, colour)
            outlineCircles.append(outlineCircle)
            
    return fillCircles, outlineCircles
              
def drawPatchII(win, colour, startPointX, startPointY):
    patchII = []
    
    xTemp = 0
    for counter in range(startPointX, startPointX+101, 10):
        p1 = Point(counter, startPointY)
        p2 = Point((startPointX+100)- xTemp , startPointY+100)
        
        line = drawLine(win, p1, p2, colour)
        
        patchII.append(line)
        xTemp +=10
        
    yTemp = 0
    for counter2 in range(startPointY, startPointY+101, 10):
        p1 = Point(startPointX, counter2)
        p2 = Point(startPointX+100, (startPointY+100)-yTemp)
        
        line2 = drawLine(win, p1, p2, colour)
        
        patchII.append(line2)
        yTemp +=10
        
    return patchII

def createWindow(patchDimension):
    
    win = GraphWin("Half Circles", patchDimension, patchDimension)
    
    win.setBackground(bgColour)
    
    return win
    
def drawCircle(win, centre, radius, colour):
    
    circle = Circle(centre, radius)
    circle.draw(win)
    circle.setFill(colour)
    circle.setOutline(colour)
    
    return circle

def drawLine(win, p1, p2, colour):
    line = Line(p1, p2)
    line.setFill(colour)
    line.draw(win)
    
    return line
    
def drawOutlineCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.draw(win)
    circle.setOutline(colour)
    
    return circle
    
def drawRectangle(win, p1, p2):
    
    rect = Rectangle(p1, p2)
    rect.draw(win)
    rect.setFill(bgColour)
    rect.setOutline(bgColour)
    
    return rect

main()