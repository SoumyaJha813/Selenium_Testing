#import all required framework
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#inherit Testcase class and create a new testcase
class PythonOrgSearch(unittest.TestCase):
    #initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        #get driver
        driver = self.driver
        #get python.org using selenium
        driver.get("https://www.python.org/")
        #assertion to confirm if the title has python keyword in it
        self.assertIn("Python", driver.title)
        #locate element by name
        elem = driver.find_element(By.NAME, "q")
        #send data
        elem.send_keys("pycon")
        #retrieve data
        elem.send_keys(Keys.RETURN)
        assert "No result found" not in driver.page_source

        time.sleep(5)
    #cleanup method calls after every test performed
    def tearDown(self):
        self.driver.close()
    #execute the script
    if __name__ == '__main__':
        unittest.main()