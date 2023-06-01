import datetime
import sys
import requests
from config import CREDENTIALS

PIXELA_URL = "https://pixe.la/"

HEADER = {
    "X-USER-TOKEN": CREDENTIALS["token"]
}


GRAPH_PARAMS = {
    "id": "coding1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

PIXELA_PARAMS = {
    "token": CREDENTIALS["token"],
    "username": CREDENTIALS["username"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
date = datetime.datetime.now()
POST_CREATION_PARAMS = {
    "date": date.strftime("%Y%m%d"),
    "quantity": sys.argv[1],
    # "optionalData": sys.argv[2],
}

USER_CREATION_EP = "v1/user"
# response = requests.post(url=PIXELA_URL+USER_CREATION_EP, json=PIXELA_PARAMS)
# print(response.text)

POST_CREATION_EP = f"/v1/users/{CREDENTIALS['username']}/graphs"
# response = requests.post(url=f"{PIXELA_URL}{POST_CREATION_EP}", json=GRAPH_PARAMS, headers=HEADER)
# print(response.text)

POST_ADD_EP = f"/v1/users/{CREDENTIALS['username']}/graphs/{GRAPH_PARAMS['id']}"
# response = requests.put(url=f"{PIXELA_URL}{POST_ADD_EP}", json=POST_CREATION_PARAMS , headers=HEADER)
# print(response.text)

PUT_PARAMS = {
    "quantity": "5",
}

# response = requests.put(url=f"{PIXELA_URL}{POST_ADD_EP}/20230529", json=PUT_PARAMS, headers=HEADER)
# print(response.text)

response = requests.delete(url=f"{PIXELA_URL}{POST_ADD_EP}/20230529", headers=HEADER)
print(response.text)
