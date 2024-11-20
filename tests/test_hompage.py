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


def test_searchbar_clickable(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    searchbar=hp.find_element(hp.search_bar)
    assert searchbar.is_displayed() and Is_clickable(searchbar)


def test_searchbar_working(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    searchbar = hp.find_element(hp.search_bar)
    hp.click_search()
    searchbar.send_keys("אושר כהן")
    time.sleep(2)
    oshercohen=hp.find_element(hp.osher_cohen)
    assert oshercohen.is_displayed()


def test_sell_visible(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    sell=hp.find_element(hp.sell_tickets)
    assert sell.is_displayed() and Is_clickable(sell)


def test_sell_website(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    sell=hp.find_element(hp.sell_tickets)
    hp.click_sell()
    time.sleep(4)
    assert driver.current_url == "https://portal-dev.safsarglobal.link/start-ticket-sell"


def test_hero_visible(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    banner=hp.find_element(hp.hero_banner)
    assert banner.is_displayed()


def test_click_theatre(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_theatre()
    assert driver.current_url == "https://portal-dev.safsarglobal.link/category-search-results/5/%D7%AA%D7%99%D7%90%D7%98%D7%A8%D7%95%D7%9F"


def test_click_music(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_music()
    assert driver.current_url == "https://portal-dev.safsarglobal.link/category-search-results/4/%D7%9E%D7%95%D7%96%D7%99%D7%A7%D7%94"



def test_click_sport(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_sport()
    assert driver.current_url == "https://portal-dev.safsarglobal.link/category-search-results/1/%D7%A1%D7%A4%D7%95%D7%A8%D7%98"


def test_click_standup(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_standup()
    assert driver.current_url == "https://portal-dev.safsarglobal.link/category-search-results/3/%D7%A1%D7%98%D7%90%D7%A0%D7%93%D7%90%D7%A4"


def test_click_kids(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_kids()
    assert driver.current_url == "https://portal-dev.safsarglobal.link/category-search-results/2/%D7%99%D7%9C%D7%93%D7%99%D7%9D"

# def test_edit(driver): //בדיקה שאפשר לעשות עריכה בעמוד של החשבון - צריך אימות טלפון
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     hp = Hp(driver)
#     driver.get(base_url)
#     time.sleep(5)
#     hp.click_login()









