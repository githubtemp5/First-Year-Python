from Vehicle import Vehicle

class Tractor(Vehicle):
    def __init__(self, numWheels, engineSize, manual, currentGear, doorsLocked, trailerAttached):
        Vehicle.__init__(self, numWheels, engineSize, manual, currentGear, doorsLocked)
        self.trailerAttached = trailerAttached
        
    def attachTrailer(self):
        if not self.trailerAttached:
            print("Trailer already attached.")
        else:
            self.trailerAttached = True
            print("Trailer Attached")