
class Pet:
    def __init__(self, name, noiseMade, species):
        self.name = name
        self.noiseMade = noiseMade
        self.species = species
        
    def makeNoise(self):
        print(self.noiseMade)
        