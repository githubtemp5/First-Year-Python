from Employee import Employee

class WeeklyPaid(Employee):
    def __init__(self, name, dateOfBirth, dateOfEmployment, jobTitle, lineManager, hourlyRate, numberHours):
        Employee.__init__(self, name, dateOfBirth, dateOfEmployment, jobTitle, lineManager)
        self.hourlyRate = hourlyRate
        self.numberHours = numberHours
    def recordHours(self, hoursToRecord):
        self.numberHours += hoursToRecord
        return self.numberHours
    def payWeeklyWage(self):
        wage = self.numberHours * self.hourlyRate
        print("Wage Paid: ", wage)
        self.numberHours = 0
        
    def changeHourlyRate(self, newRate):
        self.hourlyRate = newRate
        return self.hourlyRate
    def printEmployeeInformation(self):
        print("Employee Name: {0}\nDOB: {1}\nDOE: {2}\nJob Title: {3}\nLine Manager: {4}\nHourly Rate: {5}\nNumber of Hours:{6} ".format(self.name, self.dateOfBirth, self.dateOfEmployment, self.jobTitle, self.lineManager, self.hourlyRate, self.numberHours))