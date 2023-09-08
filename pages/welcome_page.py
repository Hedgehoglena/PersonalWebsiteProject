from pages.base_page import BasePage
from pages.welcome_page_locators import WelcomePageLocators
import time

class WelcomePage(BasePage):

    def click_view_my_credentials_btn(self):
        self.find_element(WelcomePageLocators.VIEW_MY_CREDENTIALS_BUTTON).click()

    def wait_and_click_credentials_button(self):
        self.explicitly_wait_and_find_element(5, WelcomePageLocators.CREDENTIALS_BUTTON).click()

    def verify_company_logo(self):
        time.sleep(5)
        self.capture_web_element_as_an_image(WelcomePageLocators.COMPANY_LOGO, "company_logo.png")
        return self.compare_images("company_logo.png", "company_logo.png")

