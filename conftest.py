import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():

    # Setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://demostore.supersqa.com/")


    # Run test
    yield


    # Teardown
    driver.quit()
