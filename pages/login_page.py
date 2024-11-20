from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    signup_btn=(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/div/p[2]/a')
    gmail_btn=(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/div/div/button[1]/img')

    def click_signup(self):
        self.click_element(self.signup_btn)