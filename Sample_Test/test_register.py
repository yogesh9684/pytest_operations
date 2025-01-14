import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_tear_down")
class Test_Register:
    global driver

    def test_tutorials_ninja_register(self):
        self.driver.find_element(By.XPATH,"//a[@title='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        Actual_Text = 'Your Personal Details'
        assert self.driver.find_element(By.XPATH,"//fieldset[@id='account']/legend").text.__eq__(Actual_Text)
        self.driver.find_element(By.ID,'input-firstname').send_keys('Test1')
        self.driver.find_element(By.ID,'input-lastname').send_keys('Test2')
        self.driver.find_element(By.ID, 'input-email').send_keys('test123@test.com')
        self.driver.find_element(By.ID, 'input-telephone').send_keys('123456789')
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        self.driver.find_element(By.ID,"input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME,'agree').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()


