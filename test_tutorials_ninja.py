import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_tutorials_ninja():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    expected_title = "Your Store"
    actual_title=driver.title
    time.sleep(3)
    assert actual_title == expected_title
    driver.find_element(By.XPATH,"//div[@id='search']//input").send_keys("HP")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT,'HP LP3065').is_displayed()
    driver.quit()

