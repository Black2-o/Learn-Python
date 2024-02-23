from bs4 import BeautifulSoup
import requests

URL = "https://twitter.com/ArbazRaza01"

response = requests.get(URL)

print(response.text)
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")