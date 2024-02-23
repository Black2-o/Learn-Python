import requests

url = "https://api.themoviedb.org/3/movie/671?api_key=78f7769b5b55a9b114c957e896330090"


headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
