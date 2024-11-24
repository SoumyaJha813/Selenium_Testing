import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome driver service Selenium  160->160 chrome driver
#service_obj = Service(r"C:\Users\sojha\Downloads\chromedriver-win64\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)


#locators: ID,Xpath,CSSSelector, ClassName, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("hello")
driver.find_element(By.ID, "exampleCheck1").click()

#Tagname
# Xpath - //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

#CSS - tagname[attribute='value'] -> input[type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("TobiasEthan")
assert "Success" in message
time.sleep(5)
