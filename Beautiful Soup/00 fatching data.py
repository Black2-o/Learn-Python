import requests

url = "https://timesofindia.indiatimes.com/city/delhi"

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    # print(r.text)
    with open(path, "w", encoding="utf-8") as file:
        file.write(r.text)
        

fetchAndSaveToFile(url, "Data/times.html")