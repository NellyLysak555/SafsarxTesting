import time
from pages.home_page import HomePage as Hp
from selenium.webdriver.common.by import By
from pages.music_page import MusicPage as Mp
from selenium.common.exceptions import *



def test_event_category(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    driver.get(base_url)
    time.sleep(5)
    hp.click_music()
    time.sleep(2)
    mp=Mp(driver)
    mp.click_osher_cohen()
    time.sleep(2)
    assert driver.current_url == "https://portal-dev.safsarglobal.link/event/98"