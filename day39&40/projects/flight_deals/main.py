# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

city_data = DataManager()
flight_search = FlightSearch()


for row in city_data.travel_data:
    if row["iataCode"] == "":
        iata_code = flight_search.get_iata_codes(row["city"])
        new_data = {
            "price": {
                "iataCode": iata_code
                }
            }
        city_data.put_request(row["id"], new_data)
