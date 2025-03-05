from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
lname = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
email = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
submit = driver.find_element(By.XPATH, value='/html/body/form/button')

fname.send_keys("John")
lname.send_keys("Doe")
email.send_keys("john.doe@email.com")
submit.click()