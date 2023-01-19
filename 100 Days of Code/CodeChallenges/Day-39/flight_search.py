import requests
import data_manager
from pprint import pprint




class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        json = {
            "term": city_name,
            "location_types": "city"
        }
        headers = {
            "apikey": KIWI_API_KEY
        }

        response = requests.get(url=KIWI_LOCATIONS_ENDPOINT, headers=headers, json=json)
        data = response.json()

        code = data["code"]
        return code


# json = {
#     "term": "Wichita",
#     "location_types": "city"
# }
# headers = {
#     "apikey": KIWI_API_KEY
# }
#
# response = requests.get(url=KIWI_LOCATIONS_ENDPOINT, headers=headers, params=json)
# data = response.json()
# pprint(data)


