from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_page = (By.XPATH, "//button[@class='btn btn-success']")
        self.search_country = (By.ID, "country")
        self.country_option = (By.XPATH, "//a[text()='India']")
        self.checkbox = (By.XPATH, "//label[@for='checkbox2']")
        self.purchase = (By.XPATH, "//input[@value='Purchase']")
        self.alert_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")



    def checkout(self):
        self.driver.find_element(*self.checkout_page).click()


    def select_country(self, country_name):
        self.driver.find_element(*self.search_country).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option)) #* not needed as it takes only 1 argument as tuple
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.purchase).click()

    def alert_success_msg(self):
        output_msg = self.driver.find_element(*self.alert_msg).text
        print(output_msg)
        web_msg = "Success! Thank you! Your order will be delivered in next few weeks :-)."
        assert "Success! Thank you!" in output_msg