import math
class BagOfChange:
    def __init__(self, pence1, pence2, pence5, pence10, pence20, pence50, pound1, pound2):
        self.coinQuantity = [pence1, pence2, pence5, pence10, pence20, pence50, pound1, pound2]
        self.coinInfo = [1, 2, 5, 10, 20, 50, 100, 200]
        
    def removeCoin(self, coin):
        if coin in self.coinInfo:
            position = self.coinInfo.index(coin)
            self.coinQuantity.pop(position)
            self.coinInfo.pop(position)
            print("The coin has now been removed.")
        else:
            print("Invalid Coin")
    
    def addCoin(self, coin):
        if coin in self.coinInfo:
            position = self.coinInfo.index(coin)
            self.coinQuantity[position] += 1
            print("Coin added.")
        else:
            print("Invalid coin entered.")
            
    def totalNoCoins(self):
        total = 0
        for i in range(len(self.coinQuantity)):
            total += self.coinQuantity[i]
        return total

    def totalValue(self):
        total = 0
        for i in range(len(self.coinQuantity)):
            total += (self.coinInfo[i] * self.coinQuantity[i])
        return total