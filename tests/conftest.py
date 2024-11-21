#a file that python can read it (saved name)
import  os
import pytest
from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




os.environ['WDM_LOCAL'] = '1'

# @pytest.fixture(scope="session")
# def driver():
#     firefox_options=webdriver.FirefoxOptions()
#     firefox_service=Service(GeckoDriverManager().install())
#     driver=webdriver.Firefox(service=firefox_service,options=firefox_options)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

@pytest.fixture(scope="session")
def driver():
    chrome_options=webdriver.ChromeOptions()
    chrome_service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=chrome_service,options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()