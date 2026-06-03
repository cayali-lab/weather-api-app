from weather_api import get_stockholm_weather

print("=== Weather API App ===")
print()

weather = get_stockholm_weather()

print(f"Temperature: {weather['temperature']}°C")
print(f"Wind Speed: {weather['windspeed']} km/h")
