from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import time

# @pytest.fixture(params=['chrome','firefox'], scope='class')
# def init_driver(request):
#     global driver
#     if request.param == 'chrome':
#         service = ChromeService(ChromeDriverManager(driver_version='131.0.6778.140').install())
#         driver = webdriver.Chrome(service=service)
#     elif request.param == 'firefox':
#         service = FirefoxService(GeckoDriverManager().install())
#         driver = webdriver.Firefox(service=service)
#     request.cls.driver = driver
#     yield
#     driver.quit()

@pytest.mark.usefixtures("init_driver")
class TestBase:
    pass

class TestGoogleChrome(TestBase):
    def test_chrome_title(self):
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        time.sleep(5)
        assert self.driver.title == "Google"
