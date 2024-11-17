from itertools import batched

from requests.compat import basestring
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MyAcc(BasePage):

    myacc_btn=(By.XPATH,'//*[@id="root"]/div[1]/div/nav/div[1]/ul/button')


    def click_myacc(self):
        self.click_element(self.myacc_btn)