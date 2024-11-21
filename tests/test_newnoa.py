import time
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.home_page import HomePage as Hp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_category_theater(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.theater_category))
    hp.click_theater_category()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.theater_title))
    title_text = hp.get_theater_title()
    assert "תיאטרון" in title_text


def test_category_music(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.music_category))
    hp.click_music_category()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.music_title))
    title_text = hp.get_music_title()
    assert "מוזיקה" in title_text

def test_category_sports(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.sports_category))
    hp.click_sports_category()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.sports_title))
    title_text = hp.sports_title()
    assert "ספורט" in title_text

def test_category_standup(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.standup_category))
    hp.click_standup_category()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.standup_title))
    title_text = hp.get_standup_title()
    assert "סטאנדאפ" in title_text

def test_category_kids(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.kids_category))
    hp.click_kids_category()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.kids_title))
    title_text = hp.get_kids_title()
    assert "ילדים" in title_text


def test_link_who(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.who_link))
    hp.click_who_link()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.who_title))
    title_text = hp.get_who_title()
    assert "מי אנחנו" in title_text
    driver.close()
    driver.quit()

def test_link_how(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.how_link))
    hp.click_how_link()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.how_title))
    title_text = hp.get_how_title()
    assert "איך זה עובד" in title_text
    driver.close()
    driver.quit()


def test_link_questions(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.questions_link))
    hp.click_questions_link()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.questions_title))
    title_text = hp.get_questions_title()
    assert "שאלות ותשובות" in title_text
    driver.close()
    driver.quit()

def test_link_ticket_sales(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.ticket_sales_link))
    hp.click_ticket_sales_link()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.ticket_sales_title))
    title_text = hp.get_ticket_sales_title()
    assert "מכירת כרטיסים" in title_text
    driver.close()
    driver.quit()


def test_link_contactus(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.contactus_link))
    hp.click_contactus_link()
    driver.close()
    driver.quit()


def test_link_terms(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.terms_link))
    hp.click_terms_link()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.terms_title))
    title_text = hp.get_terms_title()
    assert "תנאי שימוש" in title_text
    driver.close()
    driver.quit()

def test_link_privacy_policy(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.privacy_policy_link))
    hp.click_privacy_policy_link()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.privacy_policy_title))
    title_text = hp.get_privacy_policy_title()
    assert "מדיניות פרטיות" in title_text
    driver.close()
    driver.quit()

def test_link_cancellation_policy(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.cancellation_policy_link))
    hp.click_cancellation_policy_link()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.cancellation_policy_title))
    title_text = hp.get_cancellation_policy_title()
    assert "מדיניות ביטולים" in title_text
    driver.close()
    driver.quit()

def test_link_accessibility(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.accessibility_link))
    hp.click_accessibility_link()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.accessibility_title))
    title_text = hp.get_accessibility_title()
    assert "הצהרת נגישות" in title_text
    driver.close()
    driver.quit()

def test_button_learn_more_about_us(driver):
    base_url = "https://portal-dev.safsarglobal.link/"
    driver.get(base_url)
    hp = Hp(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(hp.learn_more_about_us_button))
    hp.click_learn_more_about_us_button()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(hp.learn_more_about_us_title))
    title_text = hp.get_learn_more_about_us_title()
    assert "מי אנחנו" in title_text
    driver.close()
    driver.quit()





