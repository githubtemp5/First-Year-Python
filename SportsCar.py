from Vehicle import Vehicle

class SportsCar(Vehicle):
    def __init__(self, numWheels, engineSize, manual, currentGear, doorsLocked, sportsMode):
        Vehicle.__init__(self, numWheels, engineSize, manual, currentGear, doorsLocked)
        self.sportsMode = sportsMode
        self.roof = "closed"
    def retractRoof(self):
        if self.roof == "open":
            self.roof = "closed"
            print("Roof retracted")
        else:
            print("Roof already closed.")
    def openRoof(self):
        if self.roof == "closed":
            self.roof = "open"
            print("Roof opened")
        else:
            print("Roof is aleady open.")
        
    def enterSportsMode(self):
        if not self.sportsMode:
            self.sportsMode = True
            print("Sports Mode ON.")
        else:
            print("Already in sports mode.")
        
            
    