import requests

def get_stockholm_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=59.33"
        "&longitude=18.07"
        "&current_weather=true"
    )

    response = requests.get(url)
    data = response.json()

    return data["current_weather"]