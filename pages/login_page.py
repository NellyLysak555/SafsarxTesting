from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    signup_btn=(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/div/p[2]/a')
    gmail_btn=(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/div/div/button[1]/img')
    email_gmail_btn=(By.XPATH,'//*[@id="identifierId"]')
    next_btn=(By.XPATH,'/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span')
    password_btn=(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')

    def click_signup(self):
        self.click_element(self.signup_btn)


    def click_gmail(self):
        self.click_element(self.gmail_btn)

    def click_my_email(self):
        self.click_element(self.email_gmail_btn)

    def click_next(self):
        self.click_element(self.next_btn)