from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

load_dotenv()

ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4169080820&f_AL=true&f_E=2&geoId=106079947&keywords=data%20engineer&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

# Click Sign in Button
time.sleep(1)
sign_in_button = driver.find_element(by=By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()

# Sign in
time.sleep(1)
email_field = driver.find_element(by=By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(2)
jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
print(len(jobs))
for job in jobs:
    # Jobs applied for to skip
    already_applied = job.find_element(By.CSS_SELECTOR, ".job-card-list__footer-wrapper")
    if already_applied.get_attribute("innerText") == "Applied":
        print("already applied")

        # Close job card on left to remove from the list
        close_applied = job.find_element(By.CSS_SELECTOR, "div button.job-card-container__action")
        close_applied.click()
        continue
    else:
        # Select job card and trigger apply pop-up
        job.click()
        time.sleep(1)
        apply = driver.find_element(By.CSS_SELECTOR, ".job-view-layout.jobs-details .jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
        apply.click()

        time.sleep(1)
        check_complex_app = driver.find_element(By.CSS_SELECTOR, "footer button")
        if check_complex_app.get_attribute("aria-label") == "Continue to next step":
            print("Don't apply to this job")
            close_app = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            close_app.click()

            # Discard app
            time.sleep(1)
            close_discard = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__confirm-dialog-btn")
            close_discard.click()

            # Close job card in left pane
            time.sleep(1)
            close_complex_card = job.find_element(By.CSS_SELECTOR, "button.job-card-container__action")
            close_complex_card.click()
            continue
        else:
           # Find the Phone number box
           number = driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--input")
           if number == "":
               number.send_keys(PHONE_NUMBER)
           else:
               send_app = driver.find_element(By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
               send_app.click()

               # Close pop-up after applying to job
               time.sleep(2)
               recruiters_popup = driver.find_element(By.CSS_SELECTOR, "button.artdeco-button--circle")
               recruiters_popup.click()
               continue

driver.quit()