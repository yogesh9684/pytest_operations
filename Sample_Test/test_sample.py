import time
import allure
from selenium.webdriver.common.by import By
import pytest



@allure.severity(allure.severity_level.MINOR)
@pytest.mark.usefixtures("setup_and_tear_down","log_on_failure")
class Test_Ninja:

    def test_tutorials_ninja(self):
        expected_title = "Your Store"
        actual_title = self.driver.title
        time.sleep(3)
        assert actual_title == expected_title
        self.driver.find_element(By.XPATH, "//div[@id='search']//input").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        assert self.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()
        self.driver.quit()
