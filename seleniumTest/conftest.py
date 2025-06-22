import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="run different browsers"
    )



@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver= webdriver.Chrome()
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver= webdriver.Firefox()
        driver.implicitly_wait(5)
    yield driver #before test execution
    driver.close() #after test execution