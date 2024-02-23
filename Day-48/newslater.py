from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "http://secure-retreat-92358.herokuapp.com/"


driver = webdriver.Chrome()
driver.get(URL)

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.TAG_NAME, "button")
fname.send_keys("Black")
lname.send_keys("2.o")
email.send_keys("black@gmail.com")
button.click()
time.sleep(100)
