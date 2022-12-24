from appExec import *
from windowUI import *

class formContents():
    def __init__(self) -> None:
        self.term = ""
        self.crn = ""
        self.email = ""
        self.sendEmail = False

    def setTerm(self, term):
        self.term = term

    def getTerm(self):
        return self.term

    def setCrn(self, crn):
        self.crn = crn

    def getCRN(self):
        return self.crn

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setSendEmail(self, sendEmail):
        self.sendEmail = sendEmail

    def getSendEmail(self):
        return self.sendEmail






