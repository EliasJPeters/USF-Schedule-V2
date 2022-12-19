from appExec import *
from windowUI import *

class formContents():
    def __init__(self) -> None:
        self.term = ""
        self.partofterm = ""
        self.campus = ""
        self.college = ""
        self.department = ""
        self.courseStatus = ""
        self.courseStatus2 = ""
        self.courseLevel = ""
        self.crn = ""
        self.subject = ""
        self.number = ""
        self.email = ""
        self.sendEmail = False

    def setTerm(self, term):
        self.term = term

    def getTerm(self):
        return self.term

    def setpartofterm(self, partofterm):
        self.partofterm = partofterm

    def getpartofterm(self):
        return self.partofterm

    def setCampus(self, campus):
        self.campus = campus

    def getCampus(self):
        return self.campus

    def setCollege(self, college):
        self.college = college

    def getCollege(self):
        return self.college

    def setDepartment(self, department):
        self.department = department

    def getDepartment(self):
        return self.department

    def setcourseStatus(self, courseStatus):
        self.courseStatus = courseStatus

    def getcourseStatus(self):
        return self.courseStatus

    def setcourseStatus2(self, courseStatus2):
        self.courseStatus2 = courseStatus2

    def getcourseStatus2(self):
        return self.courseStatus2

    def setcourseLevel(self, courseLevel):
        self.courseLevel = courseLevel

    def getcourseLevel(self):
        return self.courseLevel

    def setCrn(self, crn):
        self.crn = crn

    def getCRN(self):
        return self.crn

    def setSubject(self, subject):
        self.subject = subject

    def getSubject(self):
        return self.subject

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setSendEmail(self, sendEmail):
        self.sendEmail = sendEmail

    def getSendEmail(self):
        return self.sendEmail






