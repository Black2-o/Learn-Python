import requests
from datetime import datetime

USER_NAME = 'black2o'
TOKEN = "helloteokentestxnotfound404fount"


pixela_endpoint = "https://pixe.la/v1/users"

user_parems = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    "thanksCode":"ThisIsThanksCode"
}

# response = requests.post(url=pixela_endpoint, json=user_parems)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"


GRAPH_ID = "black69"
graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"momiji"
}

header = {
    "X-USER-TOKEN":TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers= header)
# print(graph_response.text)



post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = (datetime.now()).strftime("%Y%m%d")



post_config = {
    "date": today,
    "quantity":input("How many KM: ")
}

post_response = requests.post(url=post_endpoint, json=post_config, headers= header)
print(post_response.text)