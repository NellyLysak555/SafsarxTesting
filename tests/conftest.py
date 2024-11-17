#a file that python can read it (saved name)
import  os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



os.environ['WDM_LOCAL'] = '1'



@pytest.fixture(scope="session")
def driver():
    chrome_options=webdriver.ChromeOptions()
    chrome_service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=chrome_service,options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()