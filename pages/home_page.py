from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    login_btn=(By.XPATH, '//*[@id="root"]/div[1]/div/nav/div[1]/ul/a')


    def click_login(self):
        self.click_element(self.login_btn)





