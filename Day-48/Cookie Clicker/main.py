from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")

print(money.text)

while money != 100:
    cookie.click()


time.sleep(60)