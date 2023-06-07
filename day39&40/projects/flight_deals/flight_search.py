import requests
from config import TEQUILA


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.base_url = "https://api.tequila.kiwi.com"
        self.header = {
            "apikey": TEQUILA["apikey"],
        }
        self.params = {
            "term": "",
            "location_type": "city",
        }

    def get_iata_codes(self, city):
        self.params["term"] = city
        response = requests.get(f"{self.base_url}/locations/query", headers=self.header, params=self.params)
        response.raise_for_status()
        city_data = response.json()
        city = city_data["locations"][0]["code"]
        return city
