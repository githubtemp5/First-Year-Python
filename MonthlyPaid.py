from Employee import Employee

class MonthlyPaid(Employee):
    def __init__(self, name, dateOfBirth, dateOfEmployment, jobTitle, lineManager, monthlySalary):
        Employee.__init__(self, name, dateOfBirth, dateOfEmployment, jobTitle, lineManager)
        self.monthlySalary = monthlySalary
    def increaseMonthlySalary(self, percentage):
        self.monthlySalary += (percentage * self.monthlySalary) / 100
        return self.monthlySalary
    def printEmployeeInformation(self):
        print("Employee Name: {0}\nDOB: {1}\nDOE: {2}\nJob Title: {3}\nLine Manager: {4}\nMonthly Salary: {5}".format(self.name, self.dateOfBirth, self.dateOfEmployment, self.jobTitle, self.lineManager,self.monthlySalary))