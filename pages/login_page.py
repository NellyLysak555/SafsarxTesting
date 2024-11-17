from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    USERNAME_FIELD=(By.ID, "username")
    PASSWORD_FIELD=(By.ID,"password")
    LOGIN_BUTTON= (By.ID,"submit")


    def enter_username(self,username):
        self.enter_text(self.USERNAME_FIELD, username)


    def enter_password(self,password):
        self.enter_text(self.PASSWORD_FIELD, password)


    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)