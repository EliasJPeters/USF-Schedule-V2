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
fireFoxOptions.headless = False

website = "https://usfweb.usf.edu/DSS/StaffScheduleSearch"

def openSite():
    driver = webdriver.Firefox(options=fireFoxOptions)
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