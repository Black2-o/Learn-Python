import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

zillo = 'https://www.zillow.com/ca/rentals/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"usersSearchTerm"%3A"CA"%2C"mapBounds"%3A%7B"west"%3A-131.94092634375%2C"east"%3A-106.67237165625%2C"south"%3A27.562750297632935%2C"north"%3A46.131065706894724%7D%2C"regionSelection"%3A%5B%7B"regionId"%3A9%2C"regionType"%3A2%7D%5D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"fsba"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"ah"%3A%7B"value"%3Atrue%7D%2C"mp"%3A%7B"max"%3A5000%7D%2C"price"%3A%7B"max"%3A917919%7D%2C"sche"%3A%7B"value"%3Afalse%7D%2C"schm"%3A%7B"value"%3Afalse%7D%2C"schh"%3A%7B"value"%3Afalse%7D%2C"schp"%3A%7B"value"%3Afalse%7D%2C"schr"%3A%7B"value"%3Afalse%7D%2C"schc"%3A%7B"value"%3Afalse%7D%2C"schu"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%2C"mapZoom"%3A5%7D'

HEADERS = { 'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0"}




response = requests.get(zillo, headers=HEADERS)

code_all = response.text
# print(code_all)

soup = BeautifulSoup(code_all, "html.parser")

data = []

data_dolar = []
data_link = []
data_address = []
data_links = soup.select("ul li div article div div a")
data_dolars = soup.select("ul li div article div div.fDSTNn div span")
data_addresses = soup.select("ul li div article div div ul")

# print(data_dolars)



for x in data_dolars:
    data_dolar.append(x.text)
for x in data_links:
    if x.text == "":
        pass
    else:
        data_address.append(x.text)
        data_link.append(x["href"])

print(data_dolar)
for x in range(0, len(data_dolar)):
    data_dict = {}
    data_dict["rate"] = data_dolar[x]
    data_dict["address"] = data_address[x]
    data_dict["link"] = data_link[x]
    data.append(data_dict)


# print(data)


driver = webdriver.Chrome()

for x in data:
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfpKujT0yN1YMAv_s-0dUBtXRSJRosQPI7-aah11pMZrWzhYA/viewform')
    addressInput, priceInput, linkInput = driver.find_elements(By.CLASS_NAME, "whsOnd")


    time.sleep(2) # WAIT for input to visible in HTML
    addressInput.send_keys(x["address"])
    priceInput.send_keys(x["link"])
    linkInput.send_keys(x["rate"])


    # submit button
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').send_keys(Keys.ENTER)

    time.sleep(2) # You can remove it 


driver.quit()