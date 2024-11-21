from selenium.webdriver.common.by import By
from .base_page import BasePage



class MusicPage(BasePage):

    oshercohen=(By.XPATH,'/html/body/div/main/div[2]/div[2]/div/div[2]/div/div/div/div[1]/a')


    def click_osher_cohen(self):
        self.click_element(self.oshercohen)