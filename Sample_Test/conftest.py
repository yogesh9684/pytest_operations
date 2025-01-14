import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser')

#################################Code to Take Screenshot on Failure#############################

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
    return rep


##############################################################################

@pytest.fixture()
def setup_and_tear_down(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver=webdriver.Edge()
    else:
        print("This is not a Valid Browser")
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
