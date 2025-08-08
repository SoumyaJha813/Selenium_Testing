#the operation we perform in each page we will create a page object module with class assigned to each.
# $x("//button[@class='btn']") - console javascript
#pip install pytest-xdist - pytest -n 2 # plugin you need to run tests in parallel

#pytest -n 2 -m smoke --browser_name firefox --html=reports/report.html

import json
import time
from operator import contains

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PageObject.checkout_page import CheckoutPage
from PageObject.login_page import LoginPage
from PageObject.shopPage import ShopPage

from selenium.webdriver.chrome.options import Options

#def test_login_with_disabled_password_manager():
#test_data_path = 'C:\Users\sojha\PycharmProjects\Selenium_Testing\data\test_e2e_testframework.json'
test_data_path = '../data/test_e2e_testframework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.smoker
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    #login_page
    #Page object model - LoginPage
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)  #sending as an argument to LoginPage
    print(loginPage.getTitle())
    shop_page = loginPage.login(test_list_item["userEmail"],
                                test_list_item["userPassword"])  #as login page returns shop object

    #Page Object Model - shopPage
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())
    # driver.find_element(By.XPATH, "//a[text()='"+item_select+"']/parent::h4/parent::div/parent::div/child::div[2]/child::button").click()
    # Page object model - Checkout_page / Country select
    checkout_cntry = shop_page.add_to_cart()
    checkout_cntry.checkout()
    checkout_cntry.select_country("ind")
    checkout_cntry.alert_success_msg()
