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

def test_event_homepage(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_event()
    assert driver.current_url == "https://portal-dev.safsarglobal.link/event/93"


def test_facebook(driver): #בדיקה לחיצה על הופעה דרך קטגוריה
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_element((By.XPATH, "/html/body/div/div[2]/div[5]/div/div[2]/div[2]/li/a[2]/img"))
    assert driver.current_url == "https://www.facebook.com/people/%D7%A1%D7%A4%D7%A1%D7%A8-%D7%90%D7%99%D7%A7%D7%A1/pfbid02NWCsH5e1aeFfGiRuUZJyZM7Lom6ojAnSGterZixjQs6B76291ae2pm13F5TubUBvl/"


def test_enter_instagram(driver): #בדיקה לחיצה על אינסטגרם
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_element((By.XPATH, "/html/body/div/div[2]/div[5]/div/div[2]/div[2]/li/a[2]/img"))
    assert driver.current_url == "https://www.instagram.com/safsarx/"




