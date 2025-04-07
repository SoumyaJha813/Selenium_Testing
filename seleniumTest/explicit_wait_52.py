import time
from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.maximize_window()

driver.find_element(By.CLASS_NAME, 'search-keyword').send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
len_product = len(products)
assert len_product > 0
prod = driver.find_elements(By.XPATH, "//div[@class ='product']/h4")
item_selected = []
for element in prod:
    item_selected.append(element.text.split(' ')[0])
    print(element.text.split(' ')[0])
list_item = ['Cucumber', 'Raspberry', 'Strawberry']
assert item_selected == list_item
#Chaining concept
#//div[@class='products']/div/div/button

for product in products:
    product.find_element(By.XPATH, "div/button").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()

driver.find_element(By.XPATH, "//div[@class='cart-preview active']/div[2]/button").click()

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

assert driver.find_element(By.CLASS_NAME,"promoInfo").text == 'Code applied ..!'
def test_totalAmtsum():
    amounts = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(5) p")
    sum = 0
    for amount in amounts:
        sum += int(amount.text)
    global totalAmt
    totalAmt = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
    assert totalAmt == sum

def test_discount():
    disc = int(driver.find_element(By.CLASS_NAME, "discountPerc").text[0:2])
    print(disc)
    discAmt = ((100-disc)/100) * totalAmt
    print(discAmt)
    totalDiscAmt = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
    assert discAmt == totalDiscAmt

#test_listcheck()
test_totalAmtsum()
test_discount()

time.sleep(2)