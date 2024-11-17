from pages.login_page import LoginPage as Lp


def test_example(driver):
    base_url="https://practicetestautomation.com/practice-test-login/"
    driver.get(base_url)
    lp=Lp(driver)
    driver.get(base_url)
    lp.enter_username('student')
    lp.enter_password('Password123')
    lp.click_login()
    assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"