import time

import document
from selenium import webdriver
from selenium.webdriver.common.by import By

#chrome_options = webdriver.ChromeOptions() #adding options to run the chrom browser
#chrome_options.add_argument("headless") # when you want to run the browser as headless in background (meaning=invisible)
#chrome_options.add_argument("--ignore-certificate-errors") # ignore the warning certificate errors and proceed with Advance mode
driver = webdriver.Chrome() #adding options to driver

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veg_fruit_list = []

#get the column list of veg/fruit name - veglist
veg_fruit = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")

for v in veg_fruit:
    veg_fruit_list.append(str(v.text))
print(veg_fruit_list)

#sort the list - sortlist
sort_list = sorted(veg_fruit_list)
print("sort_list: ",sort_list)

#sortlist should be equal to veglist
assert sort_list == veg_fruit_list

time.sleep(2)