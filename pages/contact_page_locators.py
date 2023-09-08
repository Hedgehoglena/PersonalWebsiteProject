from selenium.webdriver.common.by import By


class ContactPageLocators:

    NAME_TEXT_BOX = (By.ID, "cname")
    EMAIL_TEXT_BOX = (By.ID, "cemail")
    YOUR_MESSAGE_TEXT_BOX = (By.ID, "cmessage")
    I_AGREE_TO_SUBMIT_MY_MESSAGE_BOX = (By.ID, "cterms")
    SUBMIT_MESSAGE_BUTTON = (By.XPATH, "//*[@id='contactForm']/div[5]/button")
    CONTACT_BUTTON = (By.XPATH, "//*[@id='navbarSupportedContent']/ul/li[6]/a")
    MESSAGE_TEXT_BOX = (By.ID, "cmessage")