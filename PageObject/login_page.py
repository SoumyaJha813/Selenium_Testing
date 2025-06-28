#locators are added in constructor so that there is one point of contact incase username changes.
#inside the constructor decl of var is only inside the constr - that's why we use self keyword
# self is an instance of class variable, we will attach the var to self. [self.username_input]
# driver life is defined in fixture
#* add to tuple - it will be sent as 2 argument not as tuple.
#* is used to unpack a tuple into multiple arguments, otherwise it will send the error that there is only one argument.
from selenium.webdriver.common.by import By

from PageObject.shopPage import ShopPage


class LoginPage:
    def __init__(self, driver):
        self.username_input = (By.ID, "username")
        self.password_input = (By.NAME, "password")
        self.sign_in_button = (By.ID, "signInBtn")
        self.driver = driver

    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password_input).send_keys("learning")
        self.driver.find_element(*self.sign_in_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page
