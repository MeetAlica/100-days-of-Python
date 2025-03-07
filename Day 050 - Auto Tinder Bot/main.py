from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

FB_EMAIL = "FB_EMAIL"
FB_PASSWORD = "FB_PASSWORD"

driver = webdriver.Chrome()
driver.get("http://www.tinder.com")

sleep(1)

# Click on Login
driver.find_element(By.XPATH, value='//*[text()="Log in"]').click()
driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

sleep(1)

# Change window and log in
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

driver.find_element(By.XPATH, value='//*[@id="email"]').send_keys(FB_EMAIL)
driver.find_element(By.XPATH, value='//*[@id="pass"]').send_keys(FB_PASSWORD + Keys.ENTER)

driver.switch_to.window(base_window)

sleep(1)

# Handle pop-ups
driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()
driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

# Do 100 likes
for n in range(100):

    # 1sec delay between likes
    sleep(1)

    try:
        driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]button').click()

    # Case: Matched pop-up
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a").click()

        # Case: Like button not loaded yet
        except NoSuchElementException:
            sleep(1)

driver.quit()