from test_utils import *
from pages.welcome_page import WelcomePage
from pages.credentials_page import CredentialsPage
from pages.contact_page import ContactPage
from pages.contact_success_page import ContactSuccessPage
from resources.constants import TEST_SITE_URL, MAX_ALLOWED_DIFF_PERCENTAGE
from tests.conftest import name_email_message


class TestContact:

    # Test Case 1 (Credentials button click)
    def test_credentials_button_click(self, driver):
        welcome_page = WelcomePage(driver)

        welcome_page.navigate_to(TEST_SITE_URL)
        welcome_page.wait_and_click_credentials_button()
        credentials_page = CredentialsPage(driver)

        assert credentials_page, "Credentials button is not active"

    # Test Case 2 (View My Credentials button click)
    def test_view_my_credentials_button_click(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.navigate_to((TEST_SITE_URL))
        welcome_page.click_view_my_credentials_btn()
        credentials_page = CredentialsPage(driver)
        image_url = credentials_page.wait_and_get_image_url()

        assert image_url == "http://www.elenanagovitsyna.ca/assets/images/work/1.png", "Error!, Credentials Page Not Loaded!"

        # Test Case 3 (Contact message submission)

    def test_submit_message_option(self, driver, name_email_message):
        contact_page = ContactPage(driver)
        contact_page.navigate_to(TEST_SITE_URL)
        contact_page.click_contact_btn()
        contact_page.wait_and_type_name(name_email_message[0])
        contact_page.type_email(name_email_message[1])
        contact_page.type_message(name_email_message[2])
        contact_page.click_submit_btn()

        contact_success_page = ContactSuccessPage(driver)
        message_submitted_lbl = contact_success_page.get_message_submitted_label()
        assert message_submitted_lbl, "Submission failed!"

        # Test Case 4 (Image comparison)

    def test_image_comparison(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.navigate_to(TEST_SITE_URL)
        percentage_diff = welcome_page.verify_company_logo()
        assert percentage_diff <= MAX_ALLOWED_DIFF_PERCENTAGE, f"Images are different by {percentage_diff}%"
