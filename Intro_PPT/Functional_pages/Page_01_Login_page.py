from selenium.webdriver.common.by import By

from Utility.TestBase import TestBase


class LoginPage(TestBase):

    def __init__(self, driver):
        self.driver = driver
        # self.login_btn = (By.XPATH,"//button[.//span[text()='Login']]")

        self.login_btn = (By.XPATH, "//div[text()='Start for Free']")



        self.email= (By.XPATH,"//input[@type='email']")
        # self.password = (By.XPATH,"//div[@class='pi-form-item-control-input-content']//input[@type='password']")
        self.password = (By.XPATH, "//input[@type='password']")

        self.submit_btn = (By.XPATH,"//button[@type='submit']")

    def login_btn_(self):

        try:
            if self.login_btn == self.email:
                return self.wait_element(self.email)
            else:
                return self.wait_element(self.login_btn)

        except Exception as e:
            return e



    def email_(self):
        return self.wait_element(self.email)

    def password_(self):
        return self.wait_element(self.password)

    def submit_btn_(self):
        return self.wait_element(self.submit_btn)


    def do_login(self,username,password):
        self.login_btn_().click()
        self.email_().send_keys(username)
        self.password_().send_keys(password)
        self.submit_btn_().click()
