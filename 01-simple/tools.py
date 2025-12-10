import requests
from openai import api_key
api_key = "Dwn0f2RGKABTOir+LWXttw==bjwpcCBKz0pYCVDY"


def get_weather(city:str)->dict:
    if city.lower() == "tehran":
        return request(35.7219, 51.3347)
    if city.lower() == "tabriz":
        return request(38.0792, 46.2887)
    if city.lower() == "texas":
        return request(31.9686, 99.9018)
    if city.lower() == "florida":
        return request(27.6648, 81.5158)


def request(lat:float, lon:float, api_key=api_key):
    base_url = f"https://api.api-ninjas.com/v1/weather?lat={str(lat)}&lon={str(lon)}"
    response = requests.get(base_url, headers={'X-Api-Key': api_key})

    if response.status_code != requests.codes.ok:
        print("Error:", response.status_code, response.text)
    else:
        print(response.text)


get_weather(35.7219,51.3347)
"""
tehran 35.7219° N, 51.3347° E
tabriz 38.0792° N, 46.2887° E
Texas 31.9686° N, 99.9018° W
florida 27.6648° N, 81.5158° W
"""