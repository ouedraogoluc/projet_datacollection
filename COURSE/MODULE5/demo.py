import requests
url = "https://ajayakv-rest-countries-v1.p.rapidapi.com/rest/v1/all"
headers = {
    'x-rapidapi-host': "ajayakv-rest-countries-v1.p.rapidapi.com",
    'x-rapidapi-key': "cJvLRNK0GfdM9WSMbQe3inU7REn8JVy5"
    }
response = requests.request("GET", url, headers=headers)
print(response.text)