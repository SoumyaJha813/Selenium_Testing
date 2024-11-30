import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#driver.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys("soumya.88@gmail.com")
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("soumya@gmail.com") #parent-child locator using Xpath (// /)

#driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("qwer@gmail.com") #parent
#CSS -  instead of / give space no// needed and form div:nth-child(1) input

driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("qwerty") #parent - child locator(' ' space)
#driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("qwerty")

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("qwerty")# locator - id tag
#driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#driver.find_element(By.CSS_SELECTOR, "form div:nth-child(4) button").click()
# locator - based on text
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click() #locator - based on text
time.sleep(5)