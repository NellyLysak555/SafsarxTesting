from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    login_btn=(By.XPATH, '//*[@id="root"]/div[1]/div/nav/div[1]/ul/a')
    search_bar=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div/span[1]/input')
    osher_cohen=(By.XPATH,'//*[@id="search-results-container"]/div/div[2]/div/div[2]/div/a/p')
    sell_tickets=(By.XPATH,'//*[@id="root"]/div[1]/div/nav/p')
    hero_banner=(By.XPATH,'//*[@id="root"]/div[2]/div[1]')




    def click_login(self):
        self.click_element(self.login_btn)

    def click_search(self):
        self.click_element(self.search_bar)


    def click_sell(self):
        self.click_element(self.sell_tickets)



