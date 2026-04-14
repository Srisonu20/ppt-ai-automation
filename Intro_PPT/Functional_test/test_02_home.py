import time

import pytest

from Functional_pages.Page_02_Home_page import Home_page
from Utility.TestBase import TestBase

@pytest.mark.usefixtures("login")

class TestHome:
    def test_home(self, login):

        test_hom = Home_page(login)
        time.sleep(5)

        test_hom.pi_doc_ai().click()
        time.sleep(5)

        test_hom.my_ppt_ai().click()

        time.sleep(5)

        test_hom._ppt_01().click()
        time.sleep(11.5)

        test_hom._ppt_02().click()
        time.sleep(33)


        test_hom._ppt_03().click()
        time.sleep(2)

        test_hom.driver.execute_script("window.scrollBy(0 , window.innerHeight/4);")
        time.sleep(76)



        test_hom._ppt_04().click()
        time.sleep(45)

        test_hom._ppt_05().click()
        time.sleep(34)

        # test_hom._ppt_06().click()
        # time.sleep(3)
        #
        # test_hom._ppt_07().click()
        # time.sleep(37)

        test_hom._ppt_08().click()
        time.sleep(5)

