import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.home import Home
from pages.login import Login


@pytest.mark.usefixtures("setup_local")
class TestTwo:
    @pytest.mark.regression
    def test_two(self):
        driver = self.driver
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

        # Click on create will and text will
        home.click_create_will_and_text_will()

        # Add for a contact
        home.add_for()

        # Add subject
        home.add_subject("TestDemo")

        # Add delivery
        home.add_delivery()

        # Add text
        home.add_text("This is a test case")

        # Click save emotional will
        home.click_save_emotional_will()