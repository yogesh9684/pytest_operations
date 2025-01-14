import pytest
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubspot_login(BaseTest):

    @pytest.mark.parametrize("username", (["adminlogin@gmail.com", "yogesh50008@gmail.com"]))
    def test_login_hubspotlogin(self,username):
        self.driver.get("https://app.hubspot.com/login")
        time.sleep(3)
        self.driver.find_element(By.ID,"username").send_keys(username)
        time.sleep(3)








