import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class CartPage (BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.input_flat_rate = (By.ID, "shipping_method_0_flat_rate1")
        self.checkout = (By.CLASS_NAME, "checkout-button")

    def select_flat_rate(self):
        self.click_element(self.input_flat_rate)
    
    def checkout_button(self):
        self.click_element(self.checkout)

