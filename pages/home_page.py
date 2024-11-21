from asyncio import start_server

from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    login_btn=(By.XPATH, '//*[@id="root"]/div[1]/div/nav/div[1]/ul/a')
    search_bar=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div/span[1]/input')
    osher_cohen=(By.XPATH,'//*[@id="search-results-container"]/div/div[2]/div/div[2]/div/a/p')
    sell_tickets=(By.XPATH,'//*[@id="root"]/div[1]/div/nav/p')
    hero_banner=(By.XPATH,'//*[@id="root"]/div[2]/div[1]')
    event=(By.XPATH,'//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div/div/div[1]/div/a/div[1]/img')
    music = (By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/div/div[2]/a[2]')

    theater_category = (By.XPATH, "(//span[@class='border-b-4 border-primaryPurple md:py-2 hover:border-none'])[1]")
    theater_title = (By.XPATH, "(//h1[contains(text(),'תיאטרון')])[1]")

    music_category = (By.XPATH, "(//span[@class='border-b-4 border-secondaryBlue md:py-2 hover:border-none'])[1]")
    music_title = (By.XPATH, "(//h1[contains(text(),'מוזיקה')])[1]")

    sports_category = (By.XPATH, "(//span[@class='border-b-4 border-primaryGreen md:py-2 hover:border-none'])[1]")
    sports_title = (By.XPATH, "(//h1[contains(text(),'ספורט')])[1]")

    standup_category = (By.XPATH, "(//span[@class='border-b-4 border-secondaryOrange md:py-2 hover:border-none'])[1]")
    standup_title = (By.XPATH, "(//h1[contains(text(),'סטאנדאפ')])[1]")

    kids_category = (By.XPATH, "(//span[@class='border-b-4 border-secondaryYellow md:py-2 hover:border-none'])[1]")
    kids_title = (By.XPATH, "(//h1[contains(text(),'ילדים')])[1]")

    who_link = (By.XPATH, "(//a[contains(text(),'מי אנחנו?')])[1]")
    who_title = (By.XPATH, "(//h1[contains(text(),'מי אנחנו')])[1]")

    how_link = (By.XPATH, "(//a[contains(text(),'איך זה עובד?')])[1]")
    how_title = (By.XPATH, "(//h1[contains(text(),'איך זה עובד')])[1]")

    questions_link = (By.XPATH, "(//a[contains(text(),'שאלות ותשובות')])[1]")
    questions_title = (By.XPATH, "(//h1[contains(text(),'שאלות ותשובות')])[1]")

    ticket_sales_link = (By.XPATH, "(//a[@href='/ticket-sales'])[1]")
    ticket_sales_title = (By.XPATH, "(//h1[contains(text(),'מכירת כרטיסים')])[1]")

    Contactus_link = (By.XPATH, "(//a[contains(text(),'צרו קשר')])[1]")
    Contactus_title = (By.XPATH, "(//img[@alt='Contact Us Icon'])[1]")

    terms_link = (By.XPATH, "(//a[contains(text(),'תנאי שימוש')])[1]")
    terms_title = (By.XPATH, "(//h1[contains(text(),'תנאי שימוש')])[1]")

    privacy_policy_link = (By.XPATH, "(//a[contains(text(),'מדיניות פרטיות')])[1]")
    privacy_policy_title = (By.XPATH, "(//h1[contains(text(),'מדיניות פרטיות')])[1]")

    cancellation_policy_link = (By.XPATH, "(//a[contains(text(),'מדיניות ביטולים')])[1]")
    cancellation_policy_title = (By.XPATH, "(//h1[contains(text(),'מדיניות ביטולים')])[1]")

    accessibility_link = (By.XPATH, "(//a[contains(text(),'הצהרת נגישות')])[1]")
    accessibility_title = (By.XPATH, "(//h1[contains(text(),'הצהרת נגישות')])[1]")

    learn_more_about_us_button = (By.XPATH, "(//a[contains(text(),'למדו עוד עלינו'')])[1]")
    learn_more_about_us_title = (By.XPATH, "(//h1[contains(text(),'מי אנחנו')])[1]")

    instagram_button = (By.XPATH, "(//img[@alt='instagram'])[1]")
    instagram_title = (By.XPATH, "(//h1[contains(text(),'מי אנחנו')])[1]")

    facebook_button = (By.XPATH, "(//img[@alt='facebook'])[1]")
    facebook_title = (By.XPATH, "(//h1[contains(text(),'מי אנחנו')])[1]")


    def click_music(self):
        self.click_element(self.music)

    def click_login(self):
        self.click_element(self.login_btn)

    def click_search(self):
        self.click_element(self.search_bar)


    def click_sell(self):
        self.click_element(self.sell_tickets)


    def click_event(self):
        self.click_element(self.event)

    def click_theater_category(self):
        self.click_element(self.theater_category)

    def get_theater_title(self):
        return self.find_element(self.theater_title).text

    def click_music_category(self):
         self.click_element(self.music_category)

    def get_music_title(self):
        return self.find_element(self.music_title).text


    def click_sports_category(self):
        self.click_element(self.sports_category)

    def get_sports_title(self):
        return self.find_element(self.sports_title).text


    def click_standup_category(self):
        self.click_element(self.standup_category)

    def get_standup_title(self):
        return self.find_element(self.standup_title).text

    def click_kids_category(self):
        self.click_element(self.kids_category)

    def get_kids_title(self):
        return self.find_element(self.kids_title).text

    def click_who_link(self):
        self.click_element(self.who_link)

    def get_who_title(self):
        return self.find_element(self.who_title).text

    def click_how_link(self):
        self.click_element(self.how_link)

    def get_how_title(self):
        return self.find_element(self.how_title).text

    def click_questions_link(self):
        self.click_element(self.questions_link)

    def get_questions_title(self):
        return self.find_element(self.questions_title).text

    def click_ticket_sales_link(self):
        self.click_element(self.ticket_sales_link)

    def get_ticket_sales_title(self):
        return self.find_element(self.ticket_sales_title).text

    def click_Contactus_link(self):
        self.click_element(self.Contactus_link)

    def get_Contactus_title(self):
        return self.find_element(self.Contactus_title).text


    def click_terms_link(self):
        self.click_element(self.terms_link)

    def get_terms_title(self):
        return self.find_element(self.terms_title).text

    def click_privacy_policy_link(self):
        self.click_element(self.privacy_policy_link)

    def get_privacy_policy_title(self):
        return self.find_element(self.privacy_policy_title).text

    def click_cancellation_policy_link(self):
        self.click_element(self.cancellation_policy_link)

    def get_cancellation_policy_title(self):
        return self.find_element(self.cancellation_policy_title).text

    def click_accessibility_link(self):
        self.click_element(self.accessibility_link)

    def get_accessibility_title(self):
        return self.find_element(self.accessibility_title).text

    def click_learn_more_about_us_button(self):
        self.click_element(self.learn_more_about_us_button)

    def get_learn_more_about_us_title(self):
        return self.find_element(self.learn_more_about_us_title).text

    def click_instagram_button(self):
        self.click_element(self.instagram_button)

    def get_instagram_us_title(self):
        return self.find_element(self.instagram_title).text


    def click_facebook_button(self):
        self.click_element(self.facebook_button)

    def get_facebook_title(self):
        return self.find_element(self.facebook_title).text

