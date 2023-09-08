from selenium.webdriver.common.by import By


class WelcomePageLocators:

    COMPANY_LOGO = (By.XPATH, "/html/body/header/div[2]/div[11]/div/div[2]/div/img")
    VIEW_MY_CREDENTIALS_BUTTON = (By.XPATH, "//*[@id='parallax']/div[11]/div/div[1]/div/a")
    CREDENTIALS_BUTTON = (By.XPATH, "//*[@id='navbarSupportedContent']/ul/li[4]/a")
