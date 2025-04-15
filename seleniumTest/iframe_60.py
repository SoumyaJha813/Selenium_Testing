import time
from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.switch_to.frame("mce_0_ifr")
#driver.find_element(By.ID, "tinymce").clear()
#driver.find_element(By.ID, "tinymce").send_keys("Automation testing iframe")
print(driver.find_element(By.ID, "tinymce").text)
driver.switch_to.default_content()
print(driver.find_element(By.XPATH, "//div[@class='example']/h3").text)
time.sleep(3)
