import os
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_HANDLE = os.getenv("TWITTER_HANDLE")

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Accept privacy policy
        self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]').click()
        # Start testing
        self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

        sleep(40)

        # Close popup
        self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a').click()

        # Getting speed data
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        sleep(2)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")

        sleep(2)

        # Filling email
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input').send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input').send_keys(Keys.ENTER)

        sleep(1)

        # Try password only first
        try:
            self.driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="current-password"]').send_keys(TWITTER_PASSWORD)
            self.driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="current-password"]').send_keys(Keys.ENTER)
            
        # If X asking for username
        except:
            self.driver.find_element(By.CSS_SELECTOR, value='input[data-testid="ocfEnterTextTextInput"]').send_keys(TWITTER_HANDLE)
            self.driver.find_element(By.CSS_SELECTOR, value='input[data-testid="ocfEnterTextTextInput"]').send_keys(Keys.ENTER)

            sleep(1)

            self.driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="current-password"]').send_keys(TWITTER_PASSWORD)
            self.driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="current-password"]').send_keys(Keys.ENTER)

        sleep(5)

        # Posting results
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(f"This post was created by my Python Bot. My current internet speeds are: {self.down} Mbps download, {self.up} Mbps upload")
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()

        sleep(3)
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()