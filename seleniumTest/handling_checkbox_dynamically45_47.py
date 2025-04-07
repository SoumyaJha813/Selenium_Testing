import time
from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
'''checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == 'option2':
        checkbox.click()
        assert checkbox.is_selected()
        time.sleep(1)

radio_buttons = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
for radio in radio_buttons:
    if radio.get_attribute('value') == ('radio2'):
        radio.click()
        assert radio.is_selected()
        time.sleep(1)

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
time.sleep(1)
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(1)
'''
name = 'Soumya'
driver.find_element(By.NAME, "enter-name").send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()
time.sleep(2)
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
#alert.dismiss()