from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Part 1 - Scrape the links, addresses, and prices of the rental properties
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept-Language": "hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# Create a list of the links
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]

# Create a list of the addresses
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]

# Create a list of the prices
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]


# Part 2 - Fill in the Google Form using Selenium

# Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScGfwZEZ2NM_xFzJsk0XU97JsuAXk6Piap-oXXxkO63JwngBA/viewform?usp=header")
    time.sleep(2)

    address = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()

driver.quit()