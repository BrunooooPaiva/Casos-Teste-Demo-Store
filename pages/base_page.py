import conftest
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


class BasePage:

    def __init__(self):
        self.driver = conftest.driver


    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)  
    
    def click_element(self, locator):
        self.find_element(locator).click()

    def verify_element_exist(self, locator):
        assert self.find_element(locator), f"O elemento '{locator}' não existe, mas é esperado que exista."

    def fill_in_field(self, locator, text):
        self.find_element(locator).send_keys(text)

    def fill_in_dropdown(self, locator, text):
        dropdown_countries = Select(self.find_element(locator))
        dropdown_countries.select_by_visible_text(text)




