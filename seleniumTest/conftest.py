import datetime
import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="run different browsers"
    )



@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ['call', 'setup']:
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get("browserInstance", None)
            if driver:
                # Make sure reports/screenshots directory exists
                screenshots_dir = os.path.join(os.path.dirname(__file__), 'reports', 'screenshots')
                os.makedirs(screenshots_dir, exist_ok=True)

                # Save screenshot with timestamp to avoid overwrite
                time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                test_name = report.nodeid.replace("::", "_").replace("/", "_")
                file_name = f"{test_name}_{time_stamp}.png"
                full_path = os.path.join(screenshots_dir, file_name)
                driver.get_screenshot_as_file(full_path)

                # Embed in HTML using relative path
                rel_path = os.path.join("screenshots", file_name)
                html = f'<div><img src="{rel_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))

        report.extra = extra

def _capture_screenshot( file_name, driver):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    driver.get_screenshot_as_file( file_name )
    print(f"Screenshot saved to: {file_name}")
