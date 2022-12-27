from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import windowUI
from functions import * 
from seleniumContents import *
from emailContent import *
from email_validator import validate_email, EmailNotValidError
from PyQt5.QtCore import QThread, pyqtSignal, QObject

"""
DONE:Redesign UI
Not Needed:Hidden Debug mode
DONE:Tab order in UI
DONE:Email notification based on seat availability.
DONE:Initial email notifying of enabling of email contact
DONE:Structure and frequency of emails/ info provided/included
DONE:Looped checking of seats
DONE:Change the inputInformation function variables for only Term, CRN, and email
DONE:Validate all 3 fields are valid
TODO:Threading to prevent freezing GUI - DIFFICULT BUT IMPORTANT
DONE:Get statistics running
TODO: Convert string to int, compare if seats open > 0
TODO: Multiple class support
"""

termValues = ["null","202305","202301","202208","202205","202201","202108","202105","202101","202008","202005","202001","201908","201905",
"201901","201808"]

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
        content.setCrn(testCRN())
        content.setEmail(emailDetection())
        content.setSendEmail(determineEmail(content.getEmail(), content.getCRN()))
    
    def testVariables():
        """
        print("Class value of selected term: " , content.getTerm())
        print("Class value of selected part of term: ", content.getpartofterm())
        print("Class value of selected campus: ", content.getCampus())
        print("Class value of selected college: ", content.getCollege())
        print("Class value of selected department: ", content.getDepartment())
        print("Class value of selected course status 1: ", content.getcourseStatus())
        print("Class value of selected course status 2: ", content.getcourseStatus2())
        print("Class value of selected course level: ", content.getcourseLevel())
        print("Class value of selected CRN: ", content.getCRN())
        """
        print("Term Translation: ", termTranslation())
        print("Current CRN: ", content.getCRN())
        print("Email: ", content.getEmail())
        print("Send Email?: ", content.getSendEmail())

    def testCRN():
        if len(form.crn.text()) != 0:
            if form.crn.text().isdigit() and len(form.crn.text()) == 5:
                return form.crn.text()
            else:
                return "null"
        elif len(form.crn.text()) == 0:
            return "null"
            
    def termTranslation():
        i = form.term.currentIndex()
        termValue = termValues[i]
        return termValue
    """
    def partsoftermTranslation():
        i = form.partofterm.currentIndex()
        partoftermValue = partoftermValues[i]
        return partoftermValue

    def campusTranslation():
        i = form.campus.currentIndex()
        campusValue = campusValues[i]
        return campusValue
    
    def collegeTranslation():
        i = form.college.currentIndex()
        collegeValue = collegeValues[i]
        return collegeValue

    def departmentTranslation():
        i = form.departments.currentIndex()
        departmentValue = departmentValues[i]
        return departmentValue

    def statusTranslation():
        i = form.status.currentIndex()
        statusValue = statusValues[i]
        return statusValue

    def status2Translation():
        i = form.status2.currentIndex()
        status2Value = status2Values[i]
        return status2Value

    def levelTranslation():
        i = form.level.currentIndex()
        levelValue = levelValues[i]
        return levelValue

    def subjectValidation():
        if len(form.crn_2.text()) != 0:
            if not form.crn_2.text().isdigit() and len(form.crn_2.text()) == 3:
                return form.crn_2.text()
            else: 
                #subjectError()
                return "error"
        elif len(form.crn_2.text()) == 0:
            return "null"

    def testNumber():
        if len(form.crn_5.text()) != 0:
            if form.crn_5.text().isdigit() and len(form.crn_5.text()) == 4:
                return form.crn_5.text()
            elif len(form.crn_5.text()) == 5 and not form.crn_5.text()[4].isdigit():
                return form.crn_5.text()
            else:
                #numberError()
                return "error"
        elif len(form.crn_5.text()) == 0:
            return "null"
    """
    def emailDetection():
        if len(form.emailInput.text()) == 0:
            return "null"
        elif len(form.emailInput.text()) != 0:
            try:
                v = validate_email(form.emailInput.text())
                email = v["email"]
                return email
            except EmailNotValidError as error:
                return "error"
                
    def debugBrowser():
        setVariables()
        testVariables()
        print("Debug browser function called")
        driver = openSite()
        inputInformation(driver, termTranslation(), content.getCRN())

    def testVariablesDebug():
        setVariables()
        testVariables()

    def testEmailSend():
        setVariables()
        testVariables()
        if content.getEmail() == 'error':
            print("Did not commence runtime")
            totalError(content.getSubject(), content.getEmail(), termTranslation())
        else:
            driver = openSite()
            if content.getSendEmail():
                inputInformation(driver, termTranslation(), content.getCRN())
                initialEmail(content.getCRN(),content.getEmail(),getCourseNumber(driver))
                seatEmail(content.getEmail(),getCourseNumber(driver))
                print("Email sent")
                quitDriver(driver)
            else:
                print("Email not sent.")
    
    def runtime():
        setVariables()
        if content.getEmail() == 'error':
            print("Did not commence runtime")
            totalError(content.getEmail(), content.getCRN(), termTranslation())
        else:
            if content.getSendEmail() == True and termTranslation() != "null":
                driver = openSite()
                inputInformation(driver, termTranslation(), content.getCRN())
                initialEmail(content.getCRN(),content.getEmail(),getCourseNumber(driver))
                loopedCheck(driver)
                quitDriver(driver)
                return driver
            else:
                print("Runtime not completed")
                totalError(content.getEmail(), content.getCRN(), termTranslation())
                
    

    """
    Page containing info needs to stay open so quitDriver() needs to be removed from basic runtime, unless
        the loop is before the driver quits. <---- It is
    1. Needs to refresh the page after certain amount of time (5-10 Minutes?).
    2. Needs to recheck seating data. Only seating data needs recheck, CRN and class number is still stored.
        (Exit out initial UI window and only have a tiny window open for user to confirm the program is still running? Prevents the user
        from entering another set of credentials to be reminded of more than one class. (Future update?))
    """
    def loopedCheck(driver):
        keepChecking = True
        timesChecked = 0
        timesSeatOpen = 0        
        time.sleep(3)
        while keepChecking:
            timesChecked = timesChecked + 1
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            search = driver.find_element_by_css_selector("#InnerWrapper > div.container > form > button:nth-child(15)")
            search.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            try:
                seats = (driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[13]"))
                os.system('cls')                
                print("Times Checked: ", timesChecked)
                #print("Seats open: ", seats.text)
                print("Times Unsuccessful: ", (timesChecked-timesSeatOpen))
                print("Times Successful: ", timesSeatOpen)
            #Convert to int so seat numbers like -2 are not considered open and triggers an email
                if int(seats.text) > 0:
                    seatEmail(content.getEmail(),getCourseNumber(driver), seats.text)
                    timesSeatOpen = timesSeatOpen + 1 
                form.timesCheckedValue.setText(str(timesChecked))
                form.successfulValue.setText(str(timesSeatOpen))
            except NoSuchElementException:
                print("Unable to locate seats on table!")
            
            time.sleep(60)
                

    driver = form.pushButton.clicked.connect(runtime)
    form.Debug.clicked.connect(debugBrowser)
    form.testVariables.clicked.connect(testVariablesDebug)
    form.testEmail.clicked.connect(testEmailSend)
    form.show()
    app.exec_()
    quitDriver(driver)
    

if __name__ == '__main__':
    main()
    