import time
from operator import contains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_e2e(browserInstance):
    driver = browserInstance
    #login_page
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    driver.find_element(By.NAME, "password").send_keys("learning")
    driver.find_element(By.ID, "signInBtn").click()


    #shopping_page
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # $x("//button[@class='btn']") - console javascript
    driver.find_element(By.LINK_TEXT, "Shop").click()
    # driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]") or using regex Css selector - "a[href*='shop']"
    driver.maximize_window()
    windows_open = driver.window_handles
    driver.switch_to.window(windows_open[0])
    item_select = "Samsung Note 8"
    # Chaining concept: get the Xpath of each 4 cards, do find element for each XPath(i) text
    list_phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    for i in list_phones:
        name = i.find_element(By.XPATH, "div/h4/a").text
        if name == item_select:
            i.find_element(By.XPATH, "div/button").click()

    # driver.find_element(By.XPATH, "//a[text()='"+item_select+"']/parent::h4/parent::div/parent::div/child::div[2]/child::button").click()
    driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("Ind")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='India']"))).click()
    driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
    driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

    output_msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    print(output_msg)

    web_msg = "Success! Thank you! Your order will be delivered in next few weeks :-)."
    assert "Success! Thank you!" in output_msg

    time.sleep(1)
    driver.close()