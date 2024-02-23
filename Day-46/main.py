from bs4 import BeautifulSoup
import requests

url = "https://www.billboard.com/charts/hot-100/2007-07-23"
CLIENT_ID = "53025421ed8e43e89bcef6bd1a74bf9f"

# travel_time = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# final_endpoint = url + travel_time

# web_file = requests.get(final_endpoint)
web_file = requests.get(url)

web_file_text = web_file.text

soup = BeautifulSoup(web_file_text, "html.parser")

song_names_spans = soup.select("li ul li h3")#(".chart-results h3.c-title.a-font-primary-bold-s")

song_names = [song.getText().strip() for song in song_names_spans]



