# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time
import json
import re
import pickle
from getpass import getpass
from datetime import datetime
from typing import List
from urllib.parse import urlparse
import logging
import base64
import difflib

# from PIL import image

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as EC

# import xmltojson
# import requests

baseurl = "http://localhost:8080/gopalc/addnumbers.html"
#myxpaths = {
#    "txtNum1": "//input[@name='txtNum1']",
#    "txtNum2": "//input[@name='txtNum2']",
#    "txtSum": "//input[@name='txtSum']",
#    "Submit": "//input[@name='Submit']"
#}


def foo(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f"ProgramName, {name}")  # Press Ctrl+F8 to toggle the breakpoint.
    i = 12
    j = 15
    k = i + j

    # json_objects = json.dumps(myxpaths, indent=4)
    # print(json_objects)

    # with open("fields.json", "w") as outfile:
    # json.dump(myxpaths, outfile)

    with open("fields.json", "r") as read_it:
        myxpaths = json.load(read_it)
    print(myxpaths)
    # domain = urlparse(baseurl).netloc
    # print("domain " + domain)
    driver: webdriver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.get(baseurl)
    driver.maximize_window()

    # time.sleep(5)  # Let the user actually see something!
    # print("Page tile " + driver.title)
    # content = driver.find_elements(By.XPATH,"/html/body")
    # login_form = driver.find_element_by_xpath("/html/body/form[1]")
    # print("Content")
    # print(content)
    # txtNum1: WebElement = driver.find_element(By.ID, "txtNum1")

    txtSum: WebElement = driver.find_element(By.XPATH, value=myxpaths["txtSum"])
    txtSum.clear()
    txtNum1: WebElement = driver.find_element(By.XPATH, value=myxpaths["txtNum1"])
    txtNum1.clear()
    txtNum2: WebElement = driver.find_element(By.XPATH, value=myxpaths["txtNum2"])
    txtNum2.clear()
    txtNum1.send_keys(str(i))
    txtNum2.send_keys(str(j))
    Submit: WebElement = driver.find_element(By.XPATH, value=myxpaths["Submit"])
    Submit.click()
    print("txtNum 1 : " + txtNum1.get_attribute("value"))
    print("txtNum 2 : " + txtNum2.get_attribute("value"))
    print("txtSum : " + txtSum.get_attribute("value"))
    print("Expected Value :")
    print(k)
    # Save the page content as sample.html
    with open("sample.html", "w") as html_file:
        html_file.write(txtNum1.text)
    driver.close()


# Press the green button in the gutter to run the script.

if __name__ == "__main__":
    foo("Python tomcat automation")
