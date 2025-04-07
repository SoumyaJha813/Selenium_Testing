#import necessary classes
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#create driver object
driver = webdriver.Chrome()

#A URL that delays loading
driver.get("https://www.geeksforgeeks.org")

try:
    #wait till 10s before looking for an element
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "comp")))
    time.sleep(3)
finally:
    driver.quit()
