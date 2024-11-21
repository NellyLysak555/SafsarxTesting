import time
import pytest
from unicodedata import category
from pages.login_page import LoginPage as Lp
from tests.conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


# def test_category_theater1(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     theater_category = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='border-b-4 border-primaryPurple md:py-2 hover:border-none'])[1]")))
#     theater_category.click()
#     time.sleep(2)
#     title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//h1[contains(text(),'תיאטרון')])[1]")))
#     assert "תיאטרון" in title.text
#     driver.close()
#     driver.quit()
#
# def test_category_Music2(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     Music_category = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='border-b-4 border-secondaryBlue md:py-2 hover:border-none'])[1]")))
#     Music_category.click()
#     time.sleep(2)
#     title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//h1[contains(text(),'מוזיקה')])[1]")))
#     assert "מוזיקה" in title.text
#     driver.close()
#     driver.quit()
#
#
# def test_category_Sports3(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     Sports_category = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='border-b-4 border-primaryGreen md:py-2 hover:border-none'])[1]")))
#     Sports_category.click()
#     title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//h1[contains(text(),'ספורט')])[1]")))
#     assert "ספורט" in title.text
#     time.sleep(2)
#     driver.close()
#     driver.quit()
#
# def test_category_Standup4(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     Standup_category = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='border-b-4 border-secondaryOrange md:py-2 hover:border-none'])[1]")))
#     Standup_category.click()
#     time.sleep(2)
#     title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//h1[contains(text(),'סטאנדאפ')])[1]")))
#     assert "סטאנדאפ" in title.text
#     driver.close()
#     driver.quit()
#
# def test_category_Kids5(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     Kids_category = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='border-b-4 border-secondaryYellow md:py-2 hover:border-none'])[1]")))
#     Kids_category.click()
#     time.sleep(2)
#     title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//h1[contains(text(),'ילדים')])[1]")))
#     assert "ילדים" in title.text
#     driver.close()
#     driver.quit()


# def test_link_who6(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     who_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'מי אנחנו?')])[1]")))
#     who_link.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()
#
#
# def test_link_how7(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     how_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'איך זה עובד?')])[1]")))
#     how_link.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()

# def test_link_questions8(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     questions_and_answers_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'שאלות ותשובות')])[1]")))
#     questions_and_answers_link.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()


# def test_link_ticket_sales9(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     ticket_sales_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/ticket-sales'])[1]")))
#     ticket_sales_link.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()


# def test_link_Contactus10(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     contactus_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'צרו קשר')])[1]")))
#     contactus_link.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()


# def test_link_terms11(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     terms_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'תנאי שימוש')])[1]")))
#     terms_link.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()

# def test_link_privacy_policy12(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     privacy_policy_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'מדיניות פרטיות')])[1]")))
#     privacy_policy_link.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()


# def test_link_cancellation_policy13(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     cancellation_policy_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'מדיניות ביטולים')])[1]")))
#     cancellation_policy_link.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()


# def test_link_accessibility14(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     accessibility_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'הצהרת נגישות')])[1]")))
#     accessibility_link.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()


# def test_button_instagram15(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     instagram_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//img[@alt='instagram'])[1]")))
#     time.sleep(2)
#     instagram_button.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()
#
# def test_button_facebook16(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     facebook_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//img[@alt='facebook'])[1]")))
#     time.sleep(2)
#     facebook_button.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()


# def test_button_learn_more_about_us17(driver):
#     base_url = "https://portal-dev.safsarglobal.link/"
#     driver.get(base_url)
#     time.sleep(2)
#     learn_more_about_us_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'למדו עוד עלינו')])[1]")))
#     time.sleep(2)
#     learn_more_about_us_button.click()
#     time.sleep(2)
#     driver.close()
#     driver.quit()


