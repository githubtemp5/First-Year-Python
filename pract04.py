                            #Practical 04
#Alvin Shrestha, UP826133

import os
from graphics import *

def personalGreeting():
    name=input("Enter your name: ")
    greeting="Hello "+name+", nice to see you!"
    print(greeting)

def formalName():
    fName=input("Enter your first name: ")
    lName=input("Enter your family name: ")
    formalName= fName[:1].upper()+"."+ lName.replace(lName[:1],lName[:1].upper())
    print(formalName)

def kilos2pounds():
    kilos=eval(input("Enter the weight in kilos"))
    pounds = 2.2 * float(kilos);
    print("{0:0.2f} kilos is equal to {1:0.2f} pounds".format(kilos,pounds))

def generateEmail():
    fName = input("Enter the first name: ").lower()
    lName = input("Enter the family name: ").lower()
    year = input("Enter the year you entered the university: ")
    email = lName[:4]+"."+fName[:1]+"."+year[2:]+"@myport.ac.uk"
    print(email)

def gradeTest():
    mark=input("Enter the mark between 0 and 10: ")
    
    mark = mark.replace("10","A")
    mark = mark.replace("9", "A")
    mark = mark.replace("8", "A")
    mark = mark.replace("7", "B")
    mark = mark.replace("6", "B")
    mark = mark.replace("5", "C")
    mark = mark.replace("4", "C")
    mark = mark.replace("3", "F")
    mark = mark.replace("2", "F")
    mark = mark.replace("1", "F")
    mark = mark.replace("0", "F")
    
    print(mark)
    
def gradeTest2():
    testGrade = "FFFFCCBBAAA"
    
    mark=eval(input("Enter the mark between 0 and 10: "))
    
    print("Grade is: ",testGrade[mark])

def graphicLetters():
    word = input("Enter a word to display: ")
    
    win = GraphWin("Words")
    
    for counter in range(len(word)):
        mouse = win.getMouse()
        
        text = Text(mouse, word[counter])
        text.setSize(30)
        text.draw(win)
        
def singASong():
    word = input("Enter a word: ")
    
    noOfLines = eval(input("Enter the no. of lines: "))
    
    repeat = eval(input("How many times to repeat the word? "))
    
    text = (((word+" ")*repeat)+"\n")*noOfLines
    
    print(text)

def exchangeTable():
    
    print("# "*9)
    for pounds in range(21):
        euros = pounds*1.15
        print("#{0:4}  #{1:8.2f} #".format(pounds, euros))
        
    print("# "*9)
    
def makeAcronym():
    phrase=input("Enter a phrase: ")
    phrase=phrase.split()
    
    acronym=""
    
    for counter in (phrase):
        acronym = acronym+counter[:1].upper()
        
    print(acronym)

def nameToNumber():
    name = input("Enter your name: ").lower()
    total = 0;
    
    for char in range(len(name)):
        numberEquivalent = ord(name[char])-96
        total = total + numberEquivalent
    print(total)
        
def fileInCaps():
    nameOfFile = input("Enter the name of the input file: ")
    
    #os.chdir("N:\Programs")
    file=open(nameOfFile,"r")
    
    print(file.read().upper())
    file.close()
    
def rainfallChart():
    nameOfFile = "rainfall.txt"
    #os.chdir("N:\Programs")
    file=open(nameOfFile,"r")
    
    for line in(file.readlines()):
        line=line.split()
        stars=int(line[1])
        print("{0:15}{1}".format(line[0],stars))
    file.close()

def graphicalRainfallChart():
    nameOfFile = "rainfall.txt"
    #os.chdir("N:\Programs\Data")
    win = GraphWin("Bar Chart", 700,700)
    file=open(nameOfFile,"r")
    
    diff = 50
    for textLine in(file.readlines()):
        
        textLine = textLine.split()
        
        stars = int(textLine[1])
        
        rect = Rectangle(Point(diff,600),Point(diff+45,600-stars*12))
        rect.draw(win)
        
        linex = Line(Point(40,600),Point(700,600))
        linex.draw(win)
        
        liney = Line(Point(40,600),Point(40,0))
        liney.draw(win)
        
        yLabel = Text(Point(20,600-stars*12),str(stars))
        yLabel.draw(win)
        
        xLabel = Text(Point(diff,600), textLine[0])
        print("{0:15}{1}".format(textLine[0],stars))
        
        diff=diff+50
        file.close()

def rainfallInInches():
    
    nameOfFile = "rainfall.txt"
    
    #os.chdir("N:\Programs\Data")
    
    file=open(nameOfFile,"r")
    
    textToWrite=""
    
    for line in(file.readlines()):
        line=line.split()
        stars=int(line[1])
        textToWrite=textToWrite+("{0:15}{1:0.2f}".format(line[0],stars/25.4))+"\n"
        
    print(textToWrite)
    
    file.close()
    
    outFile=open("rainfallInches.txt","w")
    
    print(textToWrite, file=outFile)
    
    outFile.close()
    
def wc():
    nameOfFile = "wordCounter.txt"
    #os.chdir("N:\Programs\Data")
    file=open(nameOfFile,"r")
    
    noOfWords=0
    noOfLines=0
    noOfCharacters=0
    
    for line in(file.readlines()):
        noOfCharacters=noOfCharacters+(len(line)-1)
        line=line.split()
        noOfWords=noOfWords+len(line)
        noOfLines=noOfLines+1
    print("Number of words:" ,noOfWords)
    print("Number of Lines:", noOfLines)
    print("Number of Characters:",noOfCharacters)
    file.close()
    
    
        
    