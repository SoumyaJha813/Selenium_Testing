import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Create a webdriver object
driver = webdriver.Chrome()

#Navigate to the website
driver.get("https://www.geeksforgeeks.org/")
#maximize the browser window
driver.maximize_window()

#locate the search icon element using Xpath
searchIcon = driver.find_element(By.XPATH, "//span[@class='flexR gs-toggle-icon']")
#click on search Icon to activate the search field
searchIcon.click()
#Locate the input field for search test using Xpath
enterText = driver.find_element(By.XPATH, "//input[@class='gs-input']")

#Enter the search query 'Data Structure' for the input field
enterText.send_keys("Data Structure")

#send the RETURN keys to submit the search query
enterText.send_keys(Keys.RETURN)

time.sleep(10)


