import math
class Lift:
    def __init__(self, maximumFloor):
        self.maxNoOfFloors = maximumFloor
        self.currentFloor = 0
        print("Current floor is: floor", self.currentFloor)
               
    def goUp(self, targetFloor):
        
        if targetFloor > self.maxNoOfFloors:
            print("Invalid floor. The lift will not move.")
        elif targetFloor < self.currentFloor:
            print("Invalid Floor. You need to go down.")
        else:
            self.floorsToMove = targetFloor - self.currentFloor
            for i in range(self.floorsToMove):
                print("Going up: floor number",self.currentFloor)
                self.currentFloor += 1
            print("The lift has arrived at floor: ", self.currentFloor)
    def goDown(self, targetFloor):
        
        if targetFloor > self.maxNoOfFloors or targetFloor <0:
            print("Invalid floor. The lift will not move")
        elif targetFloor > self.currentFloor:
            print("Invalid Floor. You need to go up.")
        else:
            self.floorsToMove = self.currentFloor - targetFloor
            for i in range(self.floorsToMove):
                print("Going down: floor number",self.currentFloor)
                self.currentFloor -=1
            print("The lift has arrived at floor: ", self.currentFloor)
    
    def callLift(self, floorCalledFrom):
        if(self.currentFloor> floorCalledFrom):
            self.goDown(floorCalledFrom)
        else:
            self.goUp(floorCalledFrom)