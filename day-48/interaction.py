from selenium import webdriver
from selenium.webdriver.common.by import By

# import selenium
# set up driver
# update chrome options
# fetch website
# find tag information

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# instantiates chrome web driver, passing along options
driver = webdriver.Chrome(options=chrome_options)

# get wiki page
driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_stats = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_stats.text)
driver.close()