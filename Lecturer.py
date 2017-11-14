import math

class Lecturer:
    def __init__(self, firstName, lastName, salary, unitsTaught):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.unitsTaught = unitsTaught
    
    def addUnits(self, unitName):
        if unitName in self.unitsTaught:
            print("Unit already exists")
        else:
            self.unitsTaught.append(unitName)
        return(self.unitsTaught)
        
    def removeUnit(self, unitName):
        if unitName in self.unitsTaught:
            self.unitsTaught.remove(unitName)
        else:
            print("Unit not present")
        return (self.unitsTaught)
        
    def givePayRise(self, risePercentage):
        newSalary = self.salary + risePercentage* (self.salary/100)
        self.salary = newSalary
        return self.salary
    def printLecturerInformation(self):
        info = "Lecturer: {0} {1} \nSalary: {2}\nUnits Taught: {3}".format(self.firstName, self.lastName, self.salary, self.unitsTaught)
        print(info)