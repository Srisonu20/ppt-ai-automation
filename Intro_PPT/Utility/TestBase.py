import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestBase:
    test_email = "shridevir843@gmail.com"
    test_paswd = "Pi@123@sonu"


    def wait_element(self,locator):
        return  WebDriverWait(self.driver,20).until(EC.presence_of_element_located(locator))


