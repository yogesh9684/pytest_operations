import time

from selenium import webdriver

def test_google():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()

def test_wikipedia():
    driver = webdriver.Chrome()
    driver.get("https://wikipedia.org")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()


def test_youtube():
    driver = webdriver.Chrome()
    driver.get("https://youtube.com")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()


def test_malegaon_sugar():
    driver = webdriver.Chrome()
    driver.get("https://malegaonsugar.com")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()

def test_Baramati():
    driver = webdriver.Chrome()
    driver.get("https://Baramati.com")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()