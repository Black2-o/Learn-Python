import requests

# api_key = "99aee0f56711dfdfbaea305dc1eef570"
# video_api_key = "69f04e4613056b159c2761a9d9e664d2"

# OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# weather_parems = {
#     "lat":26.335377,
#     "lon":88.551697,
#     # "dt":1602702000,
#     "appid": api_key
# }

# response = requests.get(OWM_ENDPOINT,params=weather_parems)


# print(response.json())


spotify_api = "53025421ed8e43e89bcef6bd1a74bf9f"

APILINK = "https://api.spotify.com"

peram ={
    "client_id":spotify_api,
    "response_type": "code",
    "redirect_uri":"http://localhost:8080/"
}

response = requests.get(APILINK,peram)
print(response.status_code)

















"""
https://api.openweathermap.org/data/2.5/roadrisk?appid={API key}
https://api.openweathermap.org/data/3.0/onecall
https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=69f04e4613056b159c2761a9d9e664d2
https://api.openweathermap.org/data/2.5/onecall
https://api.openweathermap.org/data/2.5/onecall

"""