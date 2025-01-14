from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


# @pytest.fixture(params=['chrome','firefox'], scope='class')
# def init_driver(request):
#     global driver
#     if request.param == 'chrome':
#         service = ChromeService(ChromeDriverManager(driver_version='131.0.6778.140').install())
#         driver = webdriver.Chrome(service=service)
#     elif request.param == 'firefox':
#         service = FirefoxService(GeckoDriverManager().install())
#         driver = webdriver.Firefox(service=service)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#
#     driver.quit()

# @pytest.fixture(autouse=True,scope="session")
# def Setup_and_Teardown():
#     print("Launched Browser")
#     print("Browser Opened")
#     yield
#     print("Browser Closed")
#     print("Logged out from Browser")