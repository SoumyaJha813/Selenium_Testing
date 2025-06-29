import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#__file__  - Represent the current python file
#os.path.dirname(__file__) - return the directory name seleniumTest
#os.path.join(..., '..') -  adds '..' to go one folder up Selenium_Testing
#os.path.abspath(...) - converts the relative path to an absolute full path
#sys.path.append(...) - adds the final absolute path to sys.path which is list of directory python checks when importing modules
#Real life Analogy - you're inside your room (seleniumTest) and want to grab a book from your sibling room (PageObjectSort).
# step out to hallway (..)
#walk to other room
#Add the room to your list of places to look for books (sys.path)

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PageObjectSort.sort_veg import SortVeg


def test_sort(browserInstance):
    driver = browserInstance
    # chrome_options = webdriver.ChromeOptions() #adding options to run the chrom browser
    # chrome_options.add_argument("headless") # when you want to run the browser as headless in background (meaning=invisible)
    # chrome_options.add_argument("--ignore-certificate-errors") # ignore the warning certificate errors and proceed with Advance mode
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    sortveggies = SortVeg(driver)
    sortveggies.get_veg_list()
    sortveggies.validate_sort_list()
