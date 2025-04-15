import time

import document
from selenium import webdriver

chrome_options = webdriver.ChromeOptions() #adding options to run the chrom browser
chrome_options.add_argument("headless") # when you want to run the browser as headless in background (meaning=invisible)
chrome_options.add_argument("--ignore-certificate-errors") # ignore the warning certificate errors and proceed with Advance mode
driver = webdriver.Chrome(options=chrome_options) #adding options to driver

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")

time.sleep(2)