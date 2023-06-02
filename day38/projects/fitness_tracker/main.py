import datetime as dt
import requests
from config import NUTRI_CREDENTIALS, SHEETY_CREDENTIALS, HEADER

NUTRI_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_EP = f"https://api.sheety.co/{SHEETY_CREDENTIALS['user']}/{SHEETY_CREDENTIALS['project']}/{SHEETY_CREDENTIALS['sheet']}"

NUTRI_HEADER = {
    "x-app-id": NUTRI_CREDENTIALS["APP_ID"],
    "x-app-key": NUTRI_CREDENTIALS["API_KEY"],
    "x-remote-user-id": "0"
}

SHEETY_HEADER = {
    "Authorization": SHEETY_CREDENTIALS["bearer_token"]
}

query = input("What exercises did you do?: ")

NUTRI_PARAMS = {
    "query": query,
}

response = requests.post(url=NUTRI_EP, headers=NUTRI_HEADER, json=NUTRI_PARAMS)
result = response.json()

date = dt.datetime.now().date()
time = dt.datetime.now().time()

for exercise in result["exercises"]:
    SHEETY_PARAMS = {
        "workout": {
            "date": str(date),
            "time": str(time),
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=SHEETY_EP, headers=HEADER, json=SHEETY_PARAMS)
    response.raise_for_status()
    print(response.text)
