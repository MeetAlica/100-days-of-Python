import os
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()
INSTAGRAM_EMAIL = os.getenv("INSTAGRAM_EMAIL")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
ACCOUNT = os.getenv("ACCOUNT")

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        sleep(2)

        # Login
        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(INSTAGRAM_EMAIL)
        password.send_keys(INSTAGRAM_PASSWORD)

        sleep(1)

        password.send_keys(Keys.ENTER)

        sleep(2)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}/followers")

        sleep(3)

        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(by=By.XPATH, value="//button[contains(text(), 'Follow')]")

        for button in all_buttons:
            try:
                button.click()
                sleep(1)

            # If already followed, cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()