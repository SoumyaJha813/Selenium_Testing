import time
from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element(By.XPATH, '//form/div[1]/input').send_keys("Tokyo Ghoul!!")
driver.find_element(By.NAME, "email").send_keys("ken@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("kenn")
driver.find_element(By.ID, "exampleCheck1").click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")

time.sleep(2)