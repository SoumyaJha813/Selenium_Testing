import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("smya.1@gmail.com")
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("smya.1@gmail.com") #start with 1 not 0 use tag name
#driver.find_element(By.ID, "userPassword").send_keys("smya")
#driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("smya") # 2nd div
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("smya") # CSS selector for password

#driver.find_element(By.ID,"confirmPassword").send_keys("smya")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("smya")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.LINK_TEXT, "Login").click()


time.sleep(2)