import time
from pages.myacc import MyAcc as mc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def Is_clickable(btn):
    try:
        btn.click()
        return True
    except ElementNotInteractableException:
        return False


