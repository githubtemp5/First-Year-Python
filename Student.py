import math

class Student:
    def __init__(self, fName, lName, course, feeStatus, active):
        self.fName = fName
        self.lName = lName
        self.course = course
        self.feeStatus = feeStatus
        self.active = active
        self.studentId = self.genStudentId(fName, lName)
        self.studentEmail = self.studentId +"@university.ac.uk"
        
    def genStudentId(self, fName, lName):
        studentId = fName[0].lower() + lName.lower()
        return studentId
        
    def changeCourse(self, course):
        self.course = course
        print("Course Changed")
        return course
        
    def changeFeeStatus(self):
        if self.feeStatus == "unpaid":
            self.feeStatus = "paid"
            print("Current fee status: Paid")
        else:
            self.feeStatus = "unpaid"
            print("Current fee status: Unpaid")
            
        return self.feeStatus
        
    def changeStudentStatus(self):
        if self.active:
            self.active = False
            print("Current student status: Inactive")
        else:
            self.active = True
            print("Current student status: Active")
        return self.active
        
    def retrieveInfo(self):
        info = "Student Name: {0} {1}\nCourse: {2}\nFee Status: {3}\nStudent Active: {4}\nStudentID: {5}\nStudent Email: {6}".format(self.fName, self.lName, self.course, self.feeStatus, self.active, self.studentId, self.studentEmail)
        print(info)