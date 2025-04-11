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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
actions = ActionChains(driver)
#actions.double_click()
#actions.click_and_hold()
#actions.drag_and_drop()
actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

time.sleep(2)
