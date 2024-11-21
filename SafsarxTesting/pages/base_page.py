from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver=driver


    def find_element(self,locator):  #change to wait
        return self.driver.find_element(*locator)


    def find_elements(self,locator):
        return self.driver.find_elements(*locator)



    def click_element(self,locator):
        self.find_element(locator).click()


    def enter_text(self,locator,text):
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)



