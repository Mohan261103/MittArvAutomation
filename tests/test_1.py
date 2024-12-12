import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.home import Home
from pages.login import Login


@pytest.mark.usefixtures("setup_local")
class TestOne:
    @pytest.mark.regression
    def test_one(self):
        driver =self.driver
        login=Login(driver)
        home=Home(driver)

        # Setup wait for later
        wait = WebDriverWait(driver, 10)

        # Open MittArv web application
        driver.get("https://app.mittarv.com")

        # Check we don't have other windows open already
        login.check_no_of_windows(1)

        # Wait until login page is loaded
        login.wait_until_login_page_is_loaded()

        login.verify_login_title()

        # Click on google icon
        login.click_on_google_icon()

        # Switch to google window
        login.switch_to_window(1)

        # Login via google
        login.login_to_google()

        # Switch to main window
        login.switch_to_window(0)

        # Wait until home page is loaded
        home.wait_until_main_page_loaded()

        # Click on add contact button
        home.click_on_add_contacts()

        # Add name and email
        home.add_contact_name_and_email("test","test@test.com")

        # Add phone number (India)
        home.add_phone_no("9876543210")

        # Add relation
        home.add_relation()

        # Select shortlist contact
        home.select_shortlist_contact()

        # click add contact done
        home.click_add_contact_done()