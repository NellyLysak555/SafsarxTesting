from pages.login_page import LoginPage as Lp
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





def test_signup_visible(driver): #בדיקת כפתור  הרשמה
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    login_btn=hp.find_element(hp.login_btn)
    hp.click_login()
    time.sleep(5)
    lp=Lp(driver)
    signup=lp.find_element(Lp.signup_btn)
    assert signup.is_displayed()

def test_signup_page(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_login()
    lp=Lp(driver)
    lp.click_signup()
    time.sleep(4)
    assert driver.current_url == "https://portal-dev.safsarglobal.link/register"


