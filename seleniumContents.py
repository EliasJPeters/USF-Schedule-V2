from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import QMessageBox
from appExec import *
import time

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = True
website = "https://usfweb.usf.edu/DSS/StaffScheduleSearch"

def openSite():
    driver = webdriver.Firefox(options = fireFoxOptions)
    windowHandle = driver.current_window_handle
    driver.switch_to.window(windowHandle)
    driver.get(website)
    return driver

def inputInformation(driver, term, crn):
    if term != "null":
        select = Select(driver.find_element_by_name("P_SEMESTER")) 
        select.select_by_value(term)

    if crn != "null":
        crnspot = driver.find_element_by_name("P_REF")
        crnspot.send_keys(crn)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    search = driver.find_element_by_css_selector("#InnerWrapper > div.container > form > button:nth-child(15)")
    search.click()

    time.sleep(1)

    driver.switch_to.window(driver.window_handles[1])

    time.sleep(3)
    
    numRows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr"))

    numCols=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[1]/th"))

    """
    Correct value for reading number of seats open
    seats = driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[13]")

    print("First Col: ", cols[0].text)
    print("First Row: ", rows[0].text)

    Session Xpath
    /html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[1]
    /html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[3]/td[1]

    CRN Xpath
    /html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[4]
    /html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[3]/td[4]

    print("Total Rows: " ,numRows)
    print("Total Columns: ",numCols)
    """
    
    """
    for i in range(numRows-1):
        print("Session: " , driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr["+str(i+2)+"]/td[1]").text)
        print("CRN: ", driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr["+str(i+2)+"]/td[4]").text)
        #Include course number in email
        print("Course Number: ", driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr["+str(i+2)+"]/td[5]").text)
        print("Seats Available: ", driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr["+str(i+2)+"]/td[13]").text)
        print("")
    """
    

#Returns whether or not we send an email to the user. 
#If there is an email and CRN given, we will send an email
def determineEmail(email, crn):
    if email != "null" and crn != "null":
        sendEmail = True
    else:
        sendEmail = False
    return sendEmail

def getCourseNumber(driver):
    try:
        courseNumber = (driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[5]").text)
        return courseNumber
    except NoSuchElementException:
        return "No such course Number Found"
    """
    for index, letter in enumerate(rows[0].text):
        print(index, letter.text)

    for rowNumber in range(0,1):
        print(rowNumber ,rows[rowNumber].text, "\n")

    
    results = driver.find_elements_by_xpath("//*[@id='results']/tbody")
    print(results)
    """

def getNumberSeats(driver):
    numSeats = driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[13]")
    return numSeats

def crnError():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("CRN Error")
    msg.setInformativeText('Please make sure the CRN is 5 digits and numeric.')
    msg.setWindowTitle("Error")
    msg.exec()

def totalError(email, crn, term):
    errorText = "Error(s) were found in the following field(s): \n"
    if email == "error" or email == "null":
        errorText = errorText + "-Email\n"
    if crn == "null":
        errorText = errorText + "-CRN\n"
    if term == "null":
        errorText = errorText + "-Term\n"
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error(s) Found.")
    msg.setInformativeText(errorText)
    msg.setWindowTitle("Error")
    msg.exec()

def quitDriver(driver):
    driver.quit()
    print("driver quit")
