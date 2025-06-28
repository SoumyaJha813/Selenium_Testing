#the operation we perform in each page we will create a page object module with class assigned to each.
# $x("//button[@class='btn']") - console javascript
import time
from operator import contains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.checkout_page import CheckoutPage
from PageObject.login_page import LoginPage
from PageObject.shopPage import ShopPage


from selenium.webdriver.chrome.options import Options

#def test_login_with_disabled_password_manager():


def test_e2e(browserInstance):
    driver = browserInstance
    #login_page
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    #Page object model - LoginPage
    loginPage = LoginPage(driver) #sending as an argument to LoginPage
    shop_page = loginPage.login()  #as login page returns shop object


    #Page Object Model - shopPage
    shop_page.add_product_to_cart("Samsung Note 8")

    # driver.find_element(By.XPATH, "//a[text()='"+item_select+"']/parent::h4/parent::div/parent::div/child::div[2]/child::button").click()
    # Page object model - Checkout_page / Country select
    checkout_cntry = shop_page.add_to_cart()
    checkout_cntry.checkout()
    checkout_cntry.select_country("ind")
    checkout_cntry.alert_success_msg()
