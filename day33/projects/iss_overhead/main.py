import os
import smtplib
import time
from datetime import datetime
import requests
from config import PARAMS, SMTP_DATA


# Your position is within +5 or -5 degrees of the ISS position.
def call_iss_api():
    response = requests.get(
        url="http://api.open-notify.org/iss-now.json"
        )
    response.raise_for_status()
    data = response.json()
    iss_data = {
        "lat": float(data["iss_position"]["latitude"]),
        "lng": float(data["iss_position"]["longitude"]),
    }
    return iss_data


def call_sunset_api():
    response = requests.get(
        url="https://api.sunrise-sunset.org/json",
        params=PARAMS
        )
    response.raise_for_status()
    data = response.json()
    sun_data = {
        "rise": int(data["results"]["sunrise"].split("T")[1].split(":")[0]),
        "set": int(data["results"]["sunset"].split("T")[1].split(":")[0]),
    }
    return sun_data


def is_close(iss):
    if ((PARAMS["lat"]-5 <= iss["lat"] <= PARAMS["lat"]+5) and
        (PARAMS["lng"]-5 <= iss["lng"] <= PARAMS["lng"]+5)):
        return True


def is_dark(sun):
    current_time = datetime.now()
    if sun["set"] <= current_time.hour <= sun["rise"]:
        return True


def send_email(msg=None):
    with smtplib.SMTP(SMTP_DATA["connection"]) as connection:
        connection.starttls()
        connection.login(
            user=SMTP_DATA["sender"],
            password=SMTP_DATA["password"]
            )
        connection.sendmail(
            from_addr=SMTP_DATA["sender"],
            to_addrs=SMTP_DATA["recipient"],
            msg=f"Subject:ISS overhead\n\n{msg}"
            )


def main():
    while True:
        iss_data = call_iss_api()
        sun_data = call_sunset_api()
        if is_close(iss_data) and is_dark(sun_data):
            send_email(msg="Look up")
        time.sleep(60)


os.chdir(os.path.dirname(os.path.abspath(__file__)))
main()
