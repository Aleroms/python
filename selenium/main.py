from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# instantiates chrome web driver, passing along options
driver = webdriver.Chrome(options=chrome_options)

# fetches website
driver.get(
    "https://www.santiagomorales.dev")


price = driver.find_element(By.CLASS_NAME, "title")
print(price.text)

# driver.close() # closes current tab
# closes whole app
driver.quit()
