import time
from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
country_items = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(country_items))
for country in country_items:
    if country.text == 'India':
        country.click()
        break


dynamicText = driver.find_element(By.ID, "autosuggest").get_attribute("value")
print(dynamicText)
'''
if dynamicText == "India":
    print("Found country!")
else:
    print("Not Found!")

'''
assert dynamicText == 'India'
time.sleep(2)
