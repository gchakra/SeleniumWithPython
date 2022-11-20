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
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# import xmltojson
# import json
# import requests

url = "http://localhost:8080/gopalc/addnumbers.html"


def foo(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"ProgramName, {name}")  # Press Ctrl+F8 to toggle the breakpoint.
    i = 10
    j = 15
    k = i + j

    # driver = webdriver.Chrome("C:/apps/python/chromedriver.exe")

    domain = urlparse(url).netloc
    print("domain " + domain)
    driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    driver.maximize_window()

    # time.sleep(5)  # Let the user actually see something!
    print("Page tile " + driver.title)
    content = driver.find_elements(By.XPATH,"/html/body")
    print("Content")
    print(content)
    txtNum1: WebElement = driver.find_element(By.ID, "txtNum1")
    txtNum1.send_keys(str(i))
    print("txtNum 1 : " + txtNum1.get_attribute('value'))
    txtNum2: WebElement = driver.find_element(By.ID, "txtNum2")
    txtNum2.send_keys(str(j))
    print("txtNum 2 : " + txtNum2.get_attribute('value'))
    Submit: WebElement = driver.find_element(By.ID,"Submit")
    Submit.click()
    txtSum: WebElement = driver.find_element(By.ID, "txtSum")
    print("txtSum : " + txtSum.get_attribute('value'))
    print("Expected Value :")
    print(k)
    # Save the page content as sample.html
    with open("sample.html", "w") as html_file:
        html_file.write(txtNum1.text)


    # elem2 = driver.find_element(By.NAME, "txtNum2")
    # print(elem2)
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    driver.close()


# Press the green button in the gutter to run the script.

if __name__ == "__main__":
    foo("Python tomcat automation")
