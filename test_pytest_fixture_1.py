

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import time

#For_Chrome_Browser
@pytest.fixture(scope='class')
def init_chrome_driver(request):
    service = Service(ChromeDriverManager(driver_version='131.0.6778.140').install())
    driver = webdriver.Chrome(service=service)
    request.cls.driver = driver
    yield
    driver.close()

#For_Firefox_Browser
@pytest.fixture(scope='class')
def init_firefox_driver(request):
    service = Service((GeckoDriverManager().install()))
    driver = webdriver.Firefox(service=service)
    request.cls.driver = driver
    yield
    driver.close()

#Chrome
@pytest.mark.usefixtures("init_chrome_driver")
class Test_Google_Chrome_Test():
        pass

class Test_Google_Ch(Test_Google_Chrome_Test):
    def test_chrome_title(self):
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        time.sleep(5)
        assert self.driver.title== "Google"

#Firefox
@pytest.mark.usefixtures("init_firefox_driver")
class Test_Google_Firefox_Test():
        pass

class Test_Google_FF(Test_Google_Firefox_Test):
    def test_firefox_title(self):
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        time.sleep(5)
        assert self.driver.title== "Google"

