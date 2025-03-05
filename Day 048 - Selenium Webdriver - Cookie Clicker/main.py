from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.3djake.hu/azurefilm/petg-fekete-3")

price_forint = driver.find_element(By.CLASS_NAME, value="p-price__retail")
print(f"The price is {price_forint.text}")

search_bar = driver.find_element(By.NAME, value="keyword")
print(search_bar.get_attribute("placeholder"))

# XPath
availability = driver.find_element(By.XPATH, value='//*[@id="mainWrapper"]/div/div[1]/form/div[1]/p[1]')
print(availability.text)

# driver.close()
driver.quit()