import pytest
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("*************Set Up*********************")
    service = Service("C:\\browser_drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    driver.maximize_window()

    print("****************Tear Down**********************")
    yield
    driver.quit()

def test_google(init_driver):
    assert driver.title == "Google"

def test_google_url(init_driver):
    assert driver.current_url =="https://www.google.com/"
