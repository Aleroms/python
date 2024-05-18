from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# instantiates chrome web driver, passing along options
driver = webdriver.Chrome(options=chrome_options)

# get wiki page
driver.get('https://secure-retreat-92358.herokuapp.com')

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

fname.send_keys("santiago")
lname.send_keys("morales")
email.send_keys("test2@gmail.com")

submit_btn = driver.find_element(By.TAG_NAME, value="button")
submit_btn.click()

