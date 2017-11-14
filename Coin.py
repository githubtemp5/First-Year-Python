import math
class Coin:
    def __init__(self, value):
        self.value = value
    
    def flipCoin(self):
        import random
        rand = random.random()
        print(rand)
        if(rand>=0.5):
            print("Tails")
        else:
            print("Heads")