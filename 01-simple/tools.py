import requests
api_key = "Dwn0f2RGKABTOir+LWXttw==bjwpcCBKz0pYCVDY"


def get_weather(city:str)->dict:
    if city.lower() == "tehran":
        return send_request(35.7219, 51.3347)
    if city.lower() == "tabriz":
        return send_request(38.0792, 46.2887)
    if city.lower() == "texas":
        return send_request(31.9686, 99.9018)
    if city.lower() == "florida":
        return send_request(27.6648, 81.5158)


def send_request(lat:float, lon:float, api_key=api_key):
    base_url = f"https://api.api-ninjas.com/v1/weather?lat={str(lat)}&lon={str(lon)}"
    response = requests.get(base_url, headers={'': api_key})

    if response.status_code != requests.codes.ok:
        print("Error:", response.status_code, response.text)
    else:
        print(response.text)


#get_weather(35.7219,51.3347)
send_request(35.7219, 51.3347)
"""
tehran 35.7219° N, 51.3347° E
tabriz 38.0792° N, 46.2887° E
Texas 31.9686° N, 99.9018° W
florida 27.6648° N, 81.5158° W
"""