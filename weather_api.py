import requests

CITIES = {
    "stockholm": {"name": "Stockholm", "latitude": 59.33, "longitude": 18.07},
    "goteborg": {"name": "Göteborg", "latitude": 57.71, "longitude": 11.97},
    "göteborg": {"name": "Göteborg", "latitude": 57.71, "longitude": 11.97},
    "malmo": {"name": "Malmö", "latitude": 55.60, "longitude": 13.00},
    "malmö": {"name": "Malmö", "latitude": 55.60, "longitude": 13.00},
    "uppsala": {"name": "Uppsala", "latitude": 59.86, "longitude": 17.64},
}
def get_weather_by_city(city):
    city_key = city.lower().strip()
    if city_key not in CITIES:
        return None

    selected_city = CITIES[city_key]

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={selected_city['latitude']}"
        f"&longitude={selected_city['longitude']}"
        "&current_weather=true"
    )

    response = requests.get(url)
    data = response.json()

    weather = data["current_weather"]
    weather["city"] = selected_city["name"]

    return weather


def check_api_status():
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast", timeout=5)
        if response.status_code in [200, 400]:
            return "API is online"
        return "API returned an unexpected response"
    except:
        return "API is offline"