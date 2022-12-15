from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import windowUI
from functions import * 
from seleniumContents import openSite, inputInformation

#possibleTerms = ["Summer 2023","Spring 2023","Fall 2022","Summer 2022","Spring 2022","Fall 2021","Summer 2021","Spring 2021","Fall 2020",
#"Summer 2020","Spring 2020","Fall 2019","Summer 2019","Spring 2019","Fall 2018"]

possibleTermValues = ["202305","202301","202208","202205","202201","202108","202105","202101","202008","202005","202001","201908","201905",
"201901","201808"]

possibleColleges = ["1986 Conversion College", "Acad. Support & Achievement", "Applied Arts and New Media", "Architecture & Community Desig", 
"Arts & Sciences", "Arts and Letters", "Arts and Sciences", "Arts and Sciences USFSM", "Arts and Sciences USFSP", "Basic Studies", "Behavioral & Community Science",
"Business (BA)", "Business (BU)", "Business USFSM", "Business USFSP", "Cooperative Education", "Double Major", "Early University Programs", 
"Education (ED)", "Education (EU)", "Education Joint Program", "Education Joint Program USFSP", "Education USFSM", "Education USFSP",
"Engineering", "Global Sustainability", "Graduate Studies", "Hosp & Tourism Leadership", "Human and Social Sciences", "INTO Pathway",
"Institutes and Affiliates", "Interdisciplinary Program", "Language and Literature", "Liberal Arts", "Liberal Arts & Soc Sci USFSM",
"Marine Science", "Medicine", "Natural Sciences", "New College", "No College Designated", "Nursing", "Off Campus Term / Misc", "Office of the Registrar",
"Program of Independent Studies", "Public Health", "School of Mental Hlth Studies", "Science & Mathematics USFSM", "Social and Behavioral Sciences",
"Student Admissions & Advising", "Taneja College of Pharmacy", "Technology and Innovation", "The Arts", "The Honors College", "UG Student Advising",
"USF World-Study Abroad", "Undergraduate Studies", "Undergraduate Studies USFSP", "Unused College (for stat calc)"]

possibleCollegeValues = []

class ExampleApp(QtWidgets.QMainWindow, windowUI.Ui_ClassChecker):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    content = formContents()        
    
    def setVariables():
        content.setTerm(form.term.currentText())
        content.setpartofterm(form.partofterm.currentText())
        content.setCampus(form.campus.currentText())
        content.setCollege(form.college.currentText())
        content.setDepartment(form.departments.currentText())
        content.setcourseStatus(form.status.currentText())
        content.setcourseStatus2(form.status2.currentText())
        content.setcourseLevel(form.level.currentText())
        content.setCrn(form.crn.text())
    
    def testVariables():
        print("Class value of selected term: " , content.getTerm())
        print("Class value of selected part of term: ", content.getpartofterm())
        print("Class value of selected campus: ", content.getCampus())
        print("Class value of selected college: ", content.getCollege())
        print("Class value of selected department: ", content.getDepartment())
        print("Class value of selected course status 1: ", content.getcourseStatus())
        print("Class value of selected course status 2: ", content.getcourseStatus2())
        print("Class value of selected course level: ", content.getcourseLevel())
        print("Class value of selected CRN: ", content.getCrn())
        print("Term Translation: ", termTranslation())

    def testValidation():
        if content.getCrn().isdigit():
            return True
        else:
            return False

    def termTranslation():
        i = form.term.currentIndex()
        termValue = possibleTermValues[i]
        return termValue
    
    def debugBrowser():
        setVariables()
        print("Debug browser function called")
        driver = openSite()
        inputInformation(driver, termTranslation())

    form.pushButton.clicked.connect(setVariables)
    form.pushButton.clicked.connect(testVariables)
    form.Debug.clicked.connect(debugBrowser)
    
    #form.pushButton.clicked.connect()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()