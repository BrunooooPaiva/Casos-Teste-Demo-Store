import pytest
from pages.home_page import HomePage
from pages.login_register_page import LoginRegisterPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_register_account(self):

         # Instance of object to be used in the test
        home_page = HomePage()
        login_register_page = LoginRegisterPage()

        # Check - Home Page
        home_page.verify_title_shop()
        home_page.click_on_my_account()

        # Check - My Account Page
        login_register_page.verify_title_account()
        login_register_page.values_in_the_field_register("testedemostore10001@hotmail.com", "ABC2003!@")

        login_register_page.click_button_register()

        login_register_page.verify_log_out()