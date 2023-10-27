import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage (BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.title_shop = (By.XPATH, "//h1[@class='woocommerce-products-header__title page-title']")
        self.my_account = (By.XPATH, "//a[text()='My account']")
        self.beanie = (By.XPATH, "//a[@data-product_id='16']")
        self.view_cart = (By.XPATH, "//a[@title='View cart']")

    def verify_title_shop(self):
        self.verify_element_exist(self.title_shop)

    def click_on_my_account(self):
        self.click_element(self.my_account)

    def add_beanie_in_cart(self):
        self.click_element(self.beanie)

    def button_view_cart(self):
        self.click_element(self.view_cart)

    