import requests
import json
from database import insertData

URL = 'https://restcountries.com/v3.1/all'

"""Fetch data and return data in json"""
def fetch_data(url : str):
    response = requests.get(url)
    return response.json()

""""
    Our Api return an array  
    Format data for getting only
    return array of countries formatted  
"""
def format_data() -> list:
    data = fetch_data(URL)
    countries = []
    
    for item in data:
        countries.append(
            (item.get('name').get('common'),
            item.get('area'),
            item.get('coatOfArms').get('png'))
        )
    
    return countries

    
""""
    Save Data in database 
"""
def saveData():
    result = format_data()
    if (len(result) !=0):
        print("Data getted from api successfully")
        
    insertData(result)

if __name__ == '__main__':
    print("Lanch main app")
    saveData()