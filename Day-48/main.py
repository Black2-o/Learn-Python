from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service

# chrome_driver_path = "H:\chromedriver-win64\chromedriver.exe"
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome()

# driver.get("www.google.com")

productId = "https://www.amazon.com/Gaming-Keyboard-Mouse-Combo-Mechanical/dp/B09X23WTHX/ref=sr_1_4?crid=3KNH34UD3ICKK&keywords=white+keyboard+and+mouse+wireless+combo+rgb&qid=1694095116&sprefix=white+keyboard+and+mouse+wireless+combo+rgb%2Caps%2C626&sr=8-4"
driver = webdriver.Chrome()
# driver.get(productId)

driver.get("https://www.python.org")
# time.sleep(10)
# find_element("a-offscreen")
# price = driver.find_elements(By.CSS_SELECTOR, ".a-offscreen")
# newlist = [x.text for x in price]
# print(newlist)
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)


# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(link.get_attribute("href"))

# xpath = driver.find_element(
#     By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(xpath.text)


events = driver.find_elements(
    By.CSS_SELECTOR, ".event-widget .shrubbery ul li")
main_dict = {}
event_dict = {"time": "Time",
              "Program": "Program"}

event_no = 0
for event in events:
    x = (event.text).split("\n")
    # print(x)
    event_dict["time"] = x[0]
    event_dict["Program"] = x[1]
    event_no += 1
    main_dict.update({event_no: event_dict})


print(main_dict)


driver.close()
