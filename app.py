from weather_api import get_weather_by_city, check_api_status

while True:
    print("\n====================")
    print(" Weather API App")
    print("====================")
    print("1. Show current weather by city")
    print("2. Check API status")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        print("\nAvailable cities:")
        print("- Stockholm")
        print("- Göteborg")
        print("- Malmö")
        print("- Uppsala")

        city = input("\nEnter city name: ")
        weather = get_weather_by_city(city)

        if weather is None:
            print("\nCity not found. Please try Stockholm, Göteborg, Malmö or Uppsala.")
        else:
            print("\nCurrent Weather")
            print("----------------")
            print(f"City: {weather['city']}")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Wind Speed: {weather['windspeed']} km/h")

    elif choice == "2":
        print("\n" + check_api_status())

    elif choice == "3":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid option.")
