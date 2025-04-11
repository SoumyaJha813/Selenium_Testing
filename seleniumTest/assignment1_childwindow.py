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
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "blinkingText").click()
windows_opened = driver.window_handles

driver.switch_to.window(windows_opened[1])

email = driver.find_element(By.XPATH, "//div/p[@class='im-para red']").text
print(email)

email_add = email.split(' ')[4]
print(email_add)
driver.close()
driver.switch_to.window(windows_opened[0])
driver.find_element(By.ID, "username").send_keys(email_add)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.XPATH, "//label[@class='customradio']/input[@value='admin']").click()
driver.find_element(By.ID, "terms").click()
driver.find_element(By.NAME, "signin").click()
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@style='display: block;']")))

response = driver.find_element(By.XPATH, "//div[@style='display: block;']").text
print(response)

assert "Incorrect username/password." in response

time.sleep(2)