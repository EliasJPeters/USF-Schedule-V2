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
    driver = webdriver.Firefox(options=fireFoxOptions)
    windowHandle = driver.current_window_handle
    driver.switch_to.window(windowHandle)
    driver.get(website)
    return driver

def inputInformation(driver, term, partTerm, campus, college, department, status, status2, level, crn):
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

def crnError():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("CRN Error")
    msg.setInformativeText('Please make sure the CRN is 5 digits and numeric.')
    msg.setWindowTitle("Error")
    msg.exec()