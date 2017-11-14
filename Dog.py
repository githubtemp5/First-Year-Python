from Pet import Pet

class Dog(Pet):
    def __init__(self, name, noiseMade, species):
        Pet.__init__(self, name, noiseMade, species)
    
    def chaseCat(self):
        pass
    def wagTail(self):
        print("Wiggle Wiggle")