from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

# finds element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# find the 'search' input by Name
search = driver.find_element(By.NAME, value="search")
search.send_keys("this is input entered from python into search bar", Keys.ENTER)
