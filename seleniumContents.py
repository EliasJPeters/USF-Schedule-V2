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

def inputInformation(driver, term, partTerm, campus, college, department, status, status2, level, crn, subject, number):
    if term != "null":
        select = Select(driver.find_element_by_name("P_SEMESTER")) 
        select.select_by_value(term)

    if partTerm != "null":
        select = Select(driver.find_element_by_name("P_SESSION")) 
        select.select_by_value(partTerm)

    if campus != "null":
        select = Select(driver.find_element_by_name("P_CAMPUS"))
        select.select_by_value(campus)

    if college != "null":
        select = Select(driver.find_element_by_name("P_COL"))
        select.select_by_value(college)

    if department != "null":
        select = Select(driver.find_element_by_name("P_DEPT"))
        select.select_by_value(department)

    if status != "null":
        select = Select(driver.find_element_by_name("p_status"))
        select.select_by_value(status)

    if status2 != "null":
        select = Select(driver.find_element_by_name("p_ssts_code"))
        select.select_by_value(status2)

    if level != "null":
        select = Select(driver.find_element_by_name("P_CRSE_LEVL"))
        select.select_by_value(level)

    if crn != "null":
        crnspot = driver.find_element_by_name("P_REF")
        crnspot.send_keys(crn)

    if subject != "null":
        crnspot = driver.find_element_by_name("P_SUBJ")
        crnspot.send_keys(subject)

    if number != "null":
        crnspot = driver.find_element_by_name("P_NUM")
        crnspot.send_keys(number)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    search = driver.find_element_by_css_selector("#InnerWrapper > div.container > form > button:nth-child(15)")
    search.click()

    time.sleep(1)

    driver.switch_to.window(driver.window_handles[1])

    time.sleep(3)
    
    numRows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr"))

    numCols=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[1]/th"))

    quitDriver(driver)
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
    
    for i in range(numRows-1):
        print("Session: " , driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr["+str(i+2)+"]/td[1]").text)
        print("CRN: ", driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr["+str(i+2)+"]/td[4]").text)
        print("Course Number: ", driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr["+str(i+2)+"]/td[5]").text)
        print("Seats Available: ", driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr["+str(i+2)+"]/td[13]").text)
        print("")

    firstelement = rows[0].text[0]


    for index, letter in enumerate(rows[0].text):
        print(index, letter.text)

    for rowNumber in range(0,1):
        print(rowNumber ,rows[rowNumber].text, "\n")


    results = driver.find_elements_by_xpath("//*[@id='results']/tbody")
    print(results)
    """

def crnError():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("CRN Error")
    msg.setInformativeText('Please make sure the CRN is 5 digits and numeric.')
    msg.setWindowTitle("Error")
    msg.exec()

def subjectError():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Subject Error")
    msg.setInformativeText('Please make sure the Subject is 3 letters.       (Ex: ENG)')
    msg.setWindowTitle("Error")
    msg.exec()

def numberError():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Class number Error")
    msg.setInformativeText('Please make sure the class number is 4 numbers and 1 letter (if applicable).')
    msg.setWindowTitle("Error")
    msg.exec()

def emailError():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Email Error")
    msg.setInformativeText('Please make sure the provided email is correct.')
    msg.setWindowTitle("Error")
    msg.exec()

def totalError(subject, number, email):
    errorText = "Error(s) were found in the following field(s): \n"

    if subject == "error":
        errorText = errorText + "-Subject\n"

    if number == "error":
        errorText = errorText + "-Number\n"

    if email == "error":
        errorText = errorText + "-Email\n"
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error(s) Found.")
    msg.setInformativeText(errorText)
    msg.setWindowTitle("Error")
    msg.exec()

def quitDriver(driver):
    driver.quit()
