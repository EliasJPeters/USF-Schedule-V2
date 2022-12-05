from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import windowUI
from functions import * 
from seleniumContents import openSite, inputInformation

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

    def testValidation():
        if content.getCrn().isdigit():
            return True
        else:
            return False
    
    def debugBrowser():
        setVariables()
        print("Debug browser function called")
        driver = openSite()
        inputInformation(driver, content.getTerm())

    form.pushButton.clicked.connect(setVariables)
    form.pushButton.clicked.connect(testVariables)
    form.Debug.clicked.connect(debugBrowser)
    
    #form.pushButton.clicked.connect()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()