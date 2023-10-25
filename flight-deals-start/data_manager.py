import requests
from pprint import pprint

SHEETY_GET_API = "https://api.sheety.co/401353b6eda68b0f360360a2feda82de/flightDeals/prices"
SHEETY_EDIT_API = "https://api.sheety.co/401353b6eda68b0f360360a2feda82de/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_GET_API)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_EDIT_API}/{city['id']}",
                json=new_data
            )
            print(response.text)