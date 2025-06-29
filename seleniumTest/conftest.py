import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="run different browsers"
    )



@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--incognito")
        driver= webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        driver= webdriver.Firefox()
    driver.implicitly_wait(5)

    yield driver #before test execution
    driver.close() #after test execution