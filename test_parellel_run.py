import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Initialize the Chrome WebDriver
service = Service("C:\\browser_drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

def test_google():
    driver.get("https://www.google.com")
    assert driver.title == "Google"


def test_facebook():
    driver.get("https://www.Facebook.com")
    assert driver.title == "Facebook – log in or sign up"


def test_Instagram():
    driver.get("https://www.Instagram.com")
    assert driver.title == "Instagram"


def test_wikipedia():
    driver.get("https://www.wikipedia.com")
    assert driver.title == "Wikipedia"
    driver.quit()
