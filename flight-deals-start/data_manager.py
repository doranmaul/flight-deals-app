import requests
from pprint import pprint

SHEETY_GET_API = ""
SHEETY_EDIT_API = ""

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = ""

    def get_destination_data(self):
        response = requests.get(url=SHEETY_GET_API)
        response.raise_for_status()
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

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
