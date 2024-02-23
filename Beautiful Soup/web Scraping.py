import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "/downloadhtmlfromamazon.html"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())

# spans = soup.select("div.title--wFj93")
# print(spans)