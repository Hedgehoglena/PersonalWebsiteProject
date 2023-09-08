from pages.base_page import BasePage
from pages.credentials_page_locators import CredentialsPageLocators
from pages.welcome_page_locators import WelcomePageLocators
from resources.constants import MAX_WAIT_INTERVAL


class CredentialsPage(BasePage):

    def wait_and_get_image_url(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CredentialsPageLocators.IMAGE).get_attribute(
            "src")

    def verify_company_logo(self):
        self.capture_web_element_as_an_image(WelcomePageLocators.COMPANY_LOGO, "captured_companyLogo.png")
        percentage_dif = self.compare_images("companyLogo.png", "captured_companyLogo.png")
        return percentage_dif
