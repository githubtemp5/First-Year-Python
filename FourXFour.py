from Vehicle import Vehicle

class FourXFour(Vehicle):
    def __init__(self, numWheels, engineSize, manual, currentGear, doorsLocked, offRoadMode):
        Vehicle.__init(self, numWheels, engineSize, manual, currentGear, doorsLocked)
        self.offRoadMode = offRoadMode
        
    def switchToOffroad(self):
        if self.offRoadMode:
            print("Already in off road mode.")
        else:
            self.offRoadMode = True
            print("Off Road Mode ON")
        