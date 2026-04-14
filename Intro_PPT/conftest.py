from selenium import webdriver

from Utility.TestBase import TestBase
import pytest
import time

from Functional_pages.Page_01_Login_page import LoginPage


@pytest.fixture(scope = "session")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.pi.inc")
    driver.implicitly_wait(3)
    driver.maximize_window()
    time.sleep(2)
    # request.cls.driver = driver
    yield driver
    driver.quit()



@pytest.fixture(scope="session")
def login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login_btn_().click()
    login_page.email_().send_keys(TestBase.test_email)
    login_page.password_().send_keys(TestBase.test_paswd)
    login_page.submit_btn_().click()
    return driver




