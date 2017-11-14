class Vehicle:
    def __init__(self, numWheels, engineSize, manual, currentGear, doorsLocked):
        self.numWheels = numWheels
        self.engineSize = engineSize
        self.manual = manual
        self.currentGear = currentGear
        self.doorsLocked = doorsLocked
        
    def drive(self):
        print("Vehicle now driving")
    def changeGear(self, gear):
        self.currentGear = gear
        print("Vehicle at gear: ",self.currentGear)
        return self.currentGear
    def lockDoors(self):
        if not self.doorsLocked:
            self.doorsLocked = True
            print("Doors now locked")
        else:
            print("Doors already locked.")
    def unlockDoors(self):
        if self.doorsLocked:
            self.doorsLocked = False
            print("Doors unlocked")
        else:
            print("Doors already unlocked")
        
        