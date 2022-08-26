import requests
import json

BASE_URL = "https://restcountries.com/v3.1/all"


import requests
import json


class MakeApiRestCountry:

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print(" récupérations  des données réussi  ")
            self.formatted_print(response.json())
        else:
            print(
                f"{response.status_code} erreur avec votre requête")

    def get_user_data(self, api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            print("a réussi à récupérer les données avec les paramètres fournis")
            self.formatted_print(response.json())
        else:
            print(
                f"{response.status_code} erreur avec votre requête")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):

        parameters = {
            "username": "luc"
        }
        self.get_user_data(api, parameters)


if __name__ == "__main__":
    api_call = MakeApiRestCountry(BASE_URL)

