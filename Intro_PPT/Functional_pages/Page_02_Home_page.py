
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Utility.TestBase import TestBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home_page(TestBase):
    def __init__(self,driver):
        self.driver = driver


        self.pi_doc = (By.XPATH,"//div[@data-tour='pi']")

        import  pdb
        pdb.set_trace()


        self.my_ppt = (By.XPATH,"//div[@class=' absolute inset-0 bg-transparent ']")

        self.ppt1 = (By.XPATH,"//div[text() = 'Highlights of My Professional Journey']")
        self.ppt2 = (By.XPATH,"//div[text() = 'Professional Profile']")


        self.ppt3 = (By.XPATH,"//div[text() = 'Current  Job Experience']")
        # self.ppt3_source = (By.XPATH,"//div[@class='cardTipLine']")
        # self.ppt3_source = (By.XPATH,"//div[@id='node-9395711761305288955']")
        # self.ppt3_target = (By.XPATH,"//div[@style='white-space: inherit;']/f /div[@class='_colWrapper_uhzmt_4 yor-col-wrappper'][1]")



        self.ppt4 = (By.XPATH,"//div[text() = 'Software Eng.']")
        self.ppt5 = (By.XPATH,"//div[text() = 'Software Tester']")
        # self.ppt6 = (By.XPATH,"// div[text() = 'Skills Development']")
        # self.ppt7 = (By.XPATH,"// div[text() = 'Future Aspirations']")
        self.ppt8 = (By.XPATH,"//div[text() = 'Thank You…!']")

    # // div[text() = 'Highlights of My Professional Journey']
    # // div[text() = 'Professional Profile']
    # // div[text() = 'Current  Job Experience']
    # // div[text() = 'Second Job Experience at ABC Ltd.']
    # // div[text() = 'Third Job Experience']
    # // div[text() = 'Skills Development']
    # // div[text() = 'Future Aspirations']
    # // div[text() = 'Thank You…!']


    def pi_doc_ai(self):
        return self.wait_element(self.pi_doc)

    def my_ppt_ai(self):
        return self.wait_element(self.my_ppt)

    def _ppt_01(self):
        return self.wait_element(self.ppt1)

    def _ppt_02(self):
        return self.wait_element(self.ppt2)

    def _ppt_03(self):
        return self.wait_element(self.ppt3)



        # # return self.wait_element(self.ppt3)
        # try:
        #     element = WebDriverWait(self.driver,8).until(EC.visibility_of_element_located(self.ppt3_source))
        #     actions = ActionChains(self.driver)
        #     actions.drag_and_drop_by_offset(element,0,100).perform()
        #     # actions.move_to_element(element)
        #
        # except TimeoutException:
        #     print("error")





    def _ppt_04(self):
        return self.wait_element(self.ppt4)

    def _ppt_05(self):
        return self.wait_element(self.ppt5)


    # def _ppt_06(self):
    #     return self.wait_element(self.ppt6)

    # def _ppt_07(self):
    #     return self.wait_element(self.ppt7)


    def _ppt_08(self):
        return self.wait_element(self.ppt8)

        # self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        #
        #
        # scrollable_div = self.driver.find_element(By.ID, "node-321779725261506")
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_div)

        # return element

    # def _ppt_03(self):
    #     element = self.wait_element(self.ppt3)
    #     self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", element)
    #     return element