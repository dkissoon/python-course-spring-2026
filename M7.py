# Assignment 7
# Extending Python with External Libraries and APIs
# This program uses the external "requests" library to call the Open-Meteo API,
# retrieve live weather data for New York City, parse the JSON response,
# and display the results in a clear format.

import requests

# URL for Open-Meteo forecast data
# New York City coordinates:
# latitude = 40.7128
# longitude = -74.0060
url = "https://api.open-meteo.com/v1/forecast"

# Parameters sent with the request
params = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "current": "temperature_2m,wind_speed_10m",
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "America/New_York"
}

try:
    # Send GET request to the API
    response = requests.get(url, params=params, timeout=10)

    # Raise an error if the request failed
    response.raise_for_status()

    # Convert JSON response into a Python dictionary
    data = response.json()

    # Extract selected values
    current_data = data.get("current", {})
    daily_data = data.get("daily", {})

    current_temp = current_data.get("temperature_2m")
    current_wind = current_data.get("wind_speed_10m")

    dates = daily_data.get("time", [])
    max_temps = daily_data.get("temperature_2m_max", [])
    min_temps = daily_data.get("temperature_2m_min", [])

    # Print clean output
    print("Weather Report for New York City")
    print("--------------------------------")
    print(f"Current temperature: {current_temp}°C")
    print(f"Current wind speed: {current_wind} km/h")
    print()

    print("3-Day Forecast")
    print("--------------------------------")

    # Print the first 3 days of forecast data
    for i in range(min(3, len(dates))):
        print(f"Date: {dates[i]}")
        print(f"High: {max_temps[i]}°C")
        print(f"Low: {min_temps[i]}°C")
        print()

except requests.exceptions.Timeout:
    print("Error: The request took too long. Please try again later.")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the weather service.")

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")

except ValueError:
    print("Error: The response was not valid JSON.")

except KeyError as err:
    print(f"Error: Missing expected data in the response: {err}")

except Exception as err:
    print(f"An unexpected error occurred: {err}")