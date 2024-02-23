import requests

APP_ID = "792dbfe8"
API_KEY = "f84bd179c4244094605c3d58516e4982"

api_endpooint = "https://trackapi.nutritionix.com/v2/natural/exercise"


parems = {
    "branded": True,
    "self": "big mac",
}

header = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}
response = requests.get(api_endpooint, params=parems, headers=header)
print(response)


