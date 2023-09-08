from pages.base_page import BasePage
from pages.contact_page_locators import ContactPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ContactPage(BasePage):

    def wait_and_type_name(self, name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ContactPageLocators.NAME_TEXT_BOX).send_keys(
            name)

    def type_email(self, email):
        self.find_element(ContactPageLocators.EMAIL_TEXT_BOX).send_keys(
            email)

    def type_message(self, message):
        self.find_element(ContactPageLocators.YOUR_MESSAGE_TEXT_BOX).send_keys(
            message)

    def click_check_box(self):
        self.find_element(ContactPageLocators.I_AGREE_TO_SUBMIT_MY_MESSAGE_BOX).click()

    def click_submit_btn(self):
        self.find_element(ContactPageLocators.SUBMIT_MESSAGE_BUTTON).click()

    def click_contact_btn(self):
        self.find_element(ContactPageLocators.CONTACT_BUTTON)