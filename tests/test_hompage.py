import time
from pages.home_page import HomePage as Hp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


def Is_clickable(btn):
    try:
        btn.click()
        return True
    except ElementNotInteractableException:
        return False


# def test_edit(driver): //בדיקה שאפשר לעשות עריכה בעמוד של החשבון - צריך אימות טלפון
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     hp = Hp(driver)
#     driver.get(base_url)
#     time.sleep(5)
#     hp.click_login()






def test_login(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_login()
    assert driver.current_url == "https://portal-dev.safsarglobal.link/signin"


