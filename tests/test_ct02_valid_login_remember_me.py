import pytest
from pages.home_page import HomePage
from pages.login_register_page import LoginRegisterPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login_valido_remember_me(self):

        # Instance of object to be used in the test
        home_page = HomePage()
        login_register_page = LoginRegisterPage()

        # Check - Home Page
        home_page.verify_title_shop()
        home_page.click_on_my_account()

        # Check - My Account Page
        login_register_page.verify_title_account()

        # Placing values ​​in the fields to log in
        login_register_page.values_in_the_field_login("testedemostore@hotmail.com", "ABC2003!@")
        login_register_page.click_button_remember_me()
        login_register_page.click_button_login()

        # Check - Log out (logged in)
        login_register_page.verify_log_out()