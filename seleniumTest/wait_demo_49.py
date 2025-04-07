import time
from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.maximize_window()

driver.find_element(By.CLASS_NAME, 'search-keyword').send_keys("ber")

time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
len_product = len(products)
assert len_product > 0
#Chaining concept
#//div[@class='products']/div/div/button

for product in products:
    product.find_element(By.XPATH, "div/button").click()
driver.implicitly_wait(7)
cart = driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
#time.sleep(3)
checkout = driver.find_element(By.XPATH, "//div[@class='cart-preview active']/div[2]/button").click()
#time.sleep(3)
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
#time.sleep(3)
driver.find_element(By.CLASS_NAME, "promoBtn").click()
#time.sleep(7)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

assert driver.find_element(By.CLASS_NAME,"promoInfo").text == 'Code applied ..!'

time.sleep(2)