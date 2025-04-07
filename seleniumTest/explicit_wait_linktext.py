import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#create a webdriver object
driver = webdriver.Chrome()

#get geeksforgeeks.org

driver.get("https://www.geeksforgeeks.org/")
#get element after explicitly waiting for 10sec
element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Courses ")))
element.click()
