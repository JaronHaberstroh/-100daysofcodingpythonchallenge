import os
import requests
from twilio.rest import Client
from config import PARAMS, TWILIO

weather_api_address = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(weather_api_address, params=PARAMS)
response.raise_for_status()
data = response.json()

weather_conditions = data["weather"]

is_rain = False

for condition in weather_conditions:
    if int(condition["id"]) < 800:
        is_rain = True


if is_rain:
    account_sid = TWILIO["sid"]
    auth_token = TWILIO["token"]
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Looks like rain. Better bring an umbrella.",
                        from_=TWILIO["from"],
                        to=TWILIO["to"]
                    )
    print(message.status)
else:
    account_sid = TWILIO["sid"]
    auth_token = TWILIO["token"]
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="No rain in the forseeable future. ;)",
                        from_=TWILIO["from"],
                        to=TWILIO["to"]
                    )
    print(message.status)
