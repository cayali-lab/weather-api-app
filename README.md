# weather-api-app
# Weather API App

## Short Project Summary

This project is a Python terminal application that connects to the Open-Meteo API and displays real-time weather information for different Swedish cities.

Users can view current weather conditions, check API availability, and interact with the application through a menu-based interface. The project demonstrates API integration, JSON data handling, user input validation, Git version control, and problem-solving techniques.

---

## Research Phase

During the research phase, I explored different weather APIs and compared available options. I selected the Open-Meteo API because it is free, easy to use, and provides real-time weather data without requiring an API key.

Technologies researched:

* Python
* REST APIs
* JSON
* Open-Meteo API
* Git and GitHub

### Problems and Solutions

Problem:
Understanding how REST APIs return data.

Solution:
Studied JSON responses and tested API endpoints directly in the browser.

---

## Implementation Phase

The project started by creating a GitHub repository and setting up the project structure.

Implemented features:

* Project structure creation
* GitHub integration
* SSH authentication
* Weather API integration
* Current weather display
* API status checker
* Interactive menu system
* Multi-city support

Supported cities:

* Stockholm
* Göteborg
* Malmö
* Uppsala

### Problems and Solutions

Problem:
GitHub authentication failed when using HTTPS.

Solution:
Configured SSH authentication and generated a dedicated SSH key.

Problem:
Swedish city names such as Göteborg and Malmö were not recognized correctly.

Solution:
Added support for Swedish characters and used lower().strip() to sanitize user input.

---

## Completion Phase

The application was tested using multiple city names and different menu options.

Tests completed:

* Current weather retrieval
* API status checking
* User menu navigation
* Invalid input handling
* Swedish character support

The final version successfully retrieves live weather information from the Open-Meteo API.

---

## Conclusion

This project provided practical experience in:

* Python programming
* API integration
* JSON processing
* Git and GitHub
* Troubleshooting and debugging

Future improvements may include weather forecasts, additional cities, weather details, and a graphical user interface.
