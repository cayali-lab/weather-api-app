from weather_api import get_stockholm_weather
import requests

def check_api_status():
    try:
        requests.get("https://api.open-meteo.com/v1/forecast", timeout=5)
        return "API is online"
    except:
        return "API is offline"


while True:
    print("\n====================")
    print(" Weather API App")
    print("====================")
    print("1. Show current weather")
    print("2. Check API status")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        weather = get_stockholm_weather()

        print("\nCurrent Weather")
        print("----------------")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Wind Speed: {weather['windspeed']} km/h")

    elif choice == "2":
        print("\n" + check_api_status())

    elif choice == "3":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid option.")
        