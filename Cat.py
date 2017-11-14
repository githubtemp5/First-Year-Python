from Pet import Pet

class Cat(Pet):
    def __init__(self, name, noiseMade, species):
        Pet.__init__(self, name, noiseMade, species)
    
    def scratch(self):
        print("Wrath!")
    def eatTuna(self):
        print("Eating Tuna. Yum")
    def purr(self):
        print("Purr! Purr!")