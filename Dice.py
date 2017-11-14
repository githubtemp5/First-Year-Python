import math
class Dice:
    def __init__(self, sideLabels):
        self.sideLabels = sideLabels
        self.noOfSides = len(sideLabels)
        
    def throwDice(self):
        import random
        rand = random.randint(0, self.noOfSides-1)
        output = self.sideLabels[rand]
        return output