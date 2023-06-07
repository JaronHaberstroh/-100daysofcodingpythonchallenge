from config import SHEETY
import requests

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.base_url = f"https://api.sheety.co/{SHEETY['user']}/{SHEETY['project']}/{SHEETY['sheet']}"
        self.token = {"Authorization": SHEETY["bearer_token"]}
        self.travel_data = {}
        self.get_request()


    def get_request(self):
        response = requests.get(self.base_url, headers=self.token)
        data = response.json()
        self.travel_data = data["prices"]


    def put_request(self, index, params):
        requests.put(f"{self.base_url}/{index}", headers=self.token, json=params)


    def post_request(self):
        pass


    def delete_request(self):
        pass
