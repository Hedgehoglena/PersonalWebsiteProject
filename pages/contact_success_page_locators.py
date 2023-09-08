from selenium.webdriver.common.by import By


class ContactSuccessPageLocators:
    NAME_TEXT_BOX = (By.ID, "cname")
    EMAIL_TEXT_BOX = (By.ID, "cemail")
    YOUR_MESSAGE_TEXT_BOX = (By.ID, "cmessage")
    I_AGREE_TO_SUBMIT_MY_MESSAGE_BOX = (By.ID, "cterms")
    SUBMIT_MESSAGE_BUTTON = (By.NAME, "SUBMIT MESSAGE")
    MESSAGE_SUBMITTED_LBL = (By.XPATH, "//*[@id='cmsgSubmit']")
