#import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from seleniumTest.run_InteractingWithWebpage import enterText

driver = webdriver.Chrome()

#set implicit wait
driver.implicitly_wait(10)

#get url
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
myDynamicElement = driver.find_element(By.XPATH, "//span[@class='flexR gs-toggle-icon']")
myDynamicElement.click()
enterText= driver.find_element(By.XPATH,"//input[@class='gs-input']")
enterText.send_keys("Data Structure")
enterText.send_keys(Keys.RETURN)
time.sleep(5)
