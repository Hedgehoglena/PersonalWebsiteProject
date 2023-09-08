from pages.base_page import BasePage
from pages.contact_success_page_locators import ContactSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ContactSuccessPage(BasePage):

    def get_message_submitted_label(self):
        lbl_message_submitted_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, ContactSuccessPageLocators.MESSAGE_SUBMITTED_LBL).text
        return lbl_message_submitted_txt
