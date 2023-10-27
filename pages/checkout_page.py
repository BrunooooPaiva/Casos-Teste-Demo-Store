import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class CheckoutPage (BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.checkout_title = (By.CLASS_NAME, "entry-title")
        self.first_name = (By.ID, "billing_first_name")
        self.last_name = (By.ID, "billing_last_name")
        self.company_name = (By.ID, "billing_company")
        self.country_region = (By.ID, "select2-billing_country-container")
        self.house_number_street_name = (By.ID, "billing_address_1")
        self.optional_informations = (By.ID, "billing_address_2")
        self.city = (By.ID, "billing_city")
        self.state = (By.ID, "select2-billing_state-container")
        self.postcode = (By.ID, "billing_postcode")
        self.phone = (By.ID, "billing_phone")
        self.email = (By.ID, "billing_email")
        self.notes = (By.ID, "order_comments")
        self.place_order = (By.ID, "place_order")
        self.input_country = (By.XPATH, "//input[contains(@class, 'select2-search__field')]")

        self.click_option_dropdown = (By.XPATH, "//li[contains(@class, 'select2-results__option')]")


    def verify_checkout_title(self):
        self.verify_element_exist(self.checkout_title)

    def fill_details(self, first_name, last_name, company_name, house_number_street_name, optional_informations, city, postcode, phone, email, notes):
        self.fill_in_field(self.first_name, first_name)
        self.fill_in_field(self.last_name, last_name)
        self.fill_in_field(self.company_name, company_name)
        self.fill_in_field(self.house_number_street_name, house_number_street_name)
        self.fill_in_field(self.optional_informations, optional_informations)
        self.fill_in_field(self.city, city)
        self.fill_in_field(self.postcode, postcode)
        self.fill_in_field(self.phone, phone)
        self.fill_in_field(self.email, email)
        self.fill_in_field(self.notes, notes)

    def dropdown_country_region_and_state(self, country_region, state):
        self.click_element(self.country_region)
        self.fill_in_field(self.input_country, country_region)
        self.click_element(self.click_option_dropdown)
        self.click_element(self.state)
        self.fill_in_field(self.input_country, state)
        self.click_element(self.click_option_dropdown)

    def click_button_place_hoder(self):
        self.click_element(self.place_order)

