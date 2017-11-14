from graphics import *
import random
import math

from random import random



def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageSteps)


def getInputs():
    numWalks = eval(input("How many random walks to take? "))
    numSteps = eval(input("How many steps for each walk? "))
    return numWalks, numSteps

def takeWalks(numWalks, numSteps):
    totalSteps = 0
    for walk in range(numWalks):
        stepsAway = takeAWalk(numSteps)
        totalSteps = totalSteps + stepsAway
    return totalSteps / numWalks
    
def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print("start point is", averageSteps)
    
def takeAWalk(numSteps):
 
    stepsForwardOfStart = 0
    for step in range(numSteps):
        if random() < 0.5:
            stepsForwardOfStart = stepsForwardOfStart - 1
        else:
            stepsForwardOfStart = stepsForwardOfStart + 1
    return abs(stepsForwardOfStart)

def distanceBetweenPoints(x1, y1, x2, y2):
    distance = math.sqrt((x1-x2)**2 + (y2-y1)**2)
    return distance
    
main()