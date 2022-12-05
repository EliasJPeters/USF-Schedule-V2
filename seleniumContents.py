from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
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

def inputInformation(driver, term):
    select = Select(driver.find_element_by_name("P_SEMESTER")) 
    time.sleep(1)

    #NEED TO TRANSLATE VALUES FOR FORM FML
    select.select_by_value(term)
    
    