import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/")

#CSS Selector - "tagname[attribute='value']"
driver.find_element(By.CSS_SELECTOR, "a[class='forgot-password-link']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("1")
driver.find_element(By.ID, "userPassword").send_keys("smya")
driver.find_element(By.ID, "confirmPassword").send_keys("smya")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#LINK_TEXT
driver.find_element(By.LINK_TEXT, "Login").click()

#XPATH - "//tagname[attribute='value']"
#driver.find_element(By.XPATH, "//a[@class='forgot-password-link']").click()

#ID - "id_name"
time.sleep(3)
driver.find_element(By.ID, "userEmail").send_keys("soumya.88@gmail.com")
driver.find_element(By.ID, "userPassword").send_keys("smya")
#NAME
driver.find_element(By.NAME, "login").click()
#CLASS - classname
#driver.find_element(By.CLASS_NAME, "forgot-password-link").click()



time.sleep(3)

