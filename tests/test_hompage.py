import time
from pages.home_page import HomePage as Hp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


def test_login_visible(driver): #בדיקת כפתור התחברות
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    login_btn=hp.find_element(hp.login_btn)
    assert login_btn.is_displayed()

def test_login(driver):  # בדיקת כפתור התחברות מעביר לדף התחברות
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_login()
    assert driver.current_url == "https://portal-dev.safsarglobal.link/signin"




# def test_edit(driver): //בדיקה שאפשר לעשות עריכה בעמוד של החשבון - צריך אימות טלפון
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     hp = Hp(driver)
#     driver.get(base_url)
#     time.sleep(5)
#     hp.click_login()









