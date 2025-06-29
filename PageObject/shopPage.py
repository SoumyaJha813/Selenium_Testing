from selenium.webdriver.common.by import By

from PageObject.checkout_page import CheckoutPage
from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.LINK_TEXT, "Shop")
        self.list_of_phones = (By.XPATH, "//div[@class='card h-100']")
        self.cart_link = (By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def add_product_to_cart(self, item_select):
        self.driver.find_element(*self.shop_link).click()
        # driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]") or using regex Css selector - "a[href*='shop']"
        #self.driver.maximize_window()
        #windows_open = self.driver.window_handles
        #self.driver.switch_to.window(windows_open[0])
        # Chaining concept: get the Xpath of each 4 cards, do find element for each XPath(i) text
        list_phones = self.driver.find_elements(*self.list_of_phones)
        for i in list_phones:
            name = i.find_element(By.XPATH, "div/h4/a").text
            if name == item_select:
                i.find_element(By.XPATH, "div/button").click()

    def add_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
        checkout_cntry = CheckoutPage(self.driver)
        return checkout_cntry

    def getTitle(self):
        return self.driver.title