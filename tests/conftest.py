import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def name_email_message():
    name = "Tom"
    email = "Tom@123"
    message = "Hello"
    return [name, email, message]


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()
