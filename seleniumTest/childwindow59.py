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
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()
#get all child window that are opened in form of list - 0 - 1st page, 1- 2nd page(Child window)
windowsOpened = driver.window_handles
#Child window - no scope - switch to window name
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window((windowsOpened[0]))
print(driver.find_element(By.TAG_NAME, "h3").text)
