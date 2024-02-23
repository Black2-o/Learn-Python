import requests

URL = "https://api.npoint.io/fbe2ee171668c89334d1"

response = requests.get(URL)
all_poast = response.text