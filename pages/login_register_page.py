import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginRegisterPage (BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_account = (By.XPATH, "//*[@class='page-template-default page page-id-9 wp-embed-responsive theme-storefront woocommerce-account woocommerce-page woocommerce-js storefront-full-width-content storefront-align-wide right-sidebar woocommerce-active']")
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.remember_me = (By.ID, "rememberme")
        self.log_in = (By.XPATH, "//button[text()='Log in']")
        self.log_out = (By.XPATH, "//a[text()='Log out']")
        self.reg_email = (By.ID, "reg_email")
        self.reg_password = (By.ID, "reg_password")
        self.register = (By.XPATH, "//button[text()='Register']")
        self.home = (By.LINK_TEXT, "http://demostore.supersqa.com/")

    def verify_title_account(self):
        self.verify_element_exist(self.title_account)

    def values_in_the_field_login(self, username, password):
        self.fill_in_field(self.username, username)
        self.fill_in_field(self.password, password)

    def click_button_login(self):
        self.click_element(self.log_in)
    
    def verify_log_out(self):
        self.verify_element_exist(self.log_out)

    def click_button_remember_me(self):
        self.click_element(self.remember_me)

    def values_in_the_field_register(self, email, password):
        self.fill_in_field(self.reg_email, email)
        self.fill_in_field(self.reg_password, password)

    def click_button_register(self):
        self.click_element(self.register)

    def back_to_page_home(self):
        self.click_element(self.home)