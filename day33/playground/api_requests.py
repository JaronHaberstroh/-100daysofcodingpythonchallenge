from datetime import datetime
import requests
from config import PARAMS

# # make api get request
# response = requests.get("http://api.open-notify.org/iss-now.json")
# # raise status error on exception
# response.raise_for_status()
# # get json data from response
# data = response.json()

# # get at individual parts of request
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)

response = requests.get("http://api.sunrise-sunset.org/json", params=PARAMS)
response.raise_for_status()
data = response.json()
# for key, value in data["results"].items():
    # print(f"{key}: {value}")
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

current_time = datetime.now().hour

print(sunrise)
print(current_time)
