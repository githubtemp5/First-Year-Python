import math

class Padlock:
    def __init__(self, combination):
        self.combination = str(combination)
        self.isLocked = True
        self.combinationNoDigits = len(self.combination)
        
    def openLock(self, enteredCombination):
        enteredCombination = str(enteredCombination)
        if(not self.isLocked):
            print("The padlock is already unlocked")
        elif enteredCombination == self.combination:
            self.isLocked = False
            print("Correct Combination. The padlock is unlocked.")
        else:
            print("Incorrect combination.")
            
    def closeLock(self):
        if self.isLocked:
            print("The padlock is already locked.")
        else:
            self.isLocked = True
            print("The padlock is locked.")
    def changeCombination(self, newCombination):
        newCombination = str(newCombination)
        if self.isLocked:
            print("Cannot change combination when the padlock is locked. Please unlock it first.")
        else:
            if len(newCombination) == self.combinationNoDigits:
                self.combination = newCombination
                print("The combination is now changed")
                
            else:
                print("Invalid length of combination. It has to be the same length as your current combination.")