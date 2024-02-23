import requests
import datetime

MY_LAT = 26.33338
MY_LONG = 88.55777


# response =  requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response.status_code)

# response.raise_for_status()

# data = response.json()
# print(data)

# data_position = response.json()["iss_position"]
# print(data_position)

# latitude =  data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]

# iss_position = (latitude, longitude)
# print(iss_position)

parametars = {
    # "lat":MY_LAT,
    # "lng":MY_LONG,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parametars)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


time_now = datetime.datetime.now()

print(time_now.hour)