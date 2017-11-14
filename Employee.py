
class Employee:
    def __init__(self, name, dateOfBirth, dateOfEmployment, jobTitle, lineManager):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.dateOfEmployment = dateOfEmployment
        self.jobTitle = jobTitle
        self.lineManager = lineManager
    def changeName(self, newName):
        self.name = newName
        return self.name
    def changeJobTitle(self, newTitle):
        self.jobTitle = newTitle
        return self.jobTitle
    def printEmployeeInformation(self):
        print("Employee Name: {0}\nDOB: {1}\nDOE: {2}\nJob Title: {3}\nLine Manager: {4}".format(self.name, self.dateOfBirth, self.dateOfEmployment, self.jobTitle, self.lineManager))
    def changeLineManager(self, newManager):
        self.lineManager = newManager
        return newManager
        