import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import unittest
import HtmlTestRunner


@pytest.mark.usefixtures("setup_teardown")
class TestCT04():
    def test_ct04_buy_item(self):
        home_page = HomePage()
        cart_page = CartPage()
        checkout_page = CheckoutPage()

        # Check - Home Page
        home_page.verify_title_shop()
        
        # Adding item to shopping cart and checking out
        home_page.add_beanie_in_cart()
        home_page.button_view_cart()

        # Checkout Button - Cart Page
        cart_page.select_flat_rate()
        cart_page.checkout_button()

        # Check - Checkout Page
        checkout_page.verify_checkout_title()

        # Entering data into checkout fields
        checkout_page.dropdown_country_region_and_state("United States (US)", "California")
        checkout_page.fill_details("User", "Test", "Shop Test", "Street Test, SN", "Neighborhood Test", "New York", "65364", "9999999999", "testeeeeetest@gmail.com", "No notes")
        checkout_page.click_button_place_hoder()

