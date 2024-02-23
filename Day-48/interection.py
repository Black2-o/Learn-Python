from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# count.click()
print(count.text)

view_history = driver.find_element(By.LINK_TEXT, "View history")
# view_history.click()


search = driver.find_element(By.NAME, "search")

search.send_keys("Python")
search.send_keys(Keys.ENTER)
