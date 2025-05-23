# WeatherGUI

This project, WeatherGUI, provides a simple graphical user interface (GUI) application using Python's tkinter library to display current weather information. It fetches data from the [WeatherAPI](https://www.weatherapi.com) to show real-time weather conditions for a specified city.

<!-- ![gui start screen](images/main.jpg) -->
<img src="images/main.jpg" alt="gui start screen" width="300"> <img src="images/city_info.jpg" alt="city_info" width="255">

<!-- ![city_info](images/city_info.jpg) -->

## Features:
- Displays current date and location based on user input.
- Shows weather condition (e.g., sunny, rainy) and temperature in Fahrenheit.
- Includes an icon representing the current weather condition fetched dynamically from the WeatherAPI.

## Components:
- gui.py: Contains the tkinter-based GUI code to interact with users and display weather information.
- weather_automation.py: Handles API requests and data parsing using the [WeatherAPI](https://www.weatherapi.com/) to fetch current weather details.

## How to Use:
- Run gui.py.
- Enter the name of the city for which you want to check the weather. (To be more specific, you can also add the state in this format: City, State)
- Click "Submit" to display weather details including date, location, weather condition, temperature, and an icon representing the weather.

## Dependencies:
- Python 3
- tkinter
- Pillow (PIL)
- requests

## 🔐 API Key Setup

This app requires an API key from [WeatherAPI](https://www.weatherapi.com/) to fetch weather data.

1. Sign up at [weatherapi.com](https://www.weatherapi.com/) to get your free API key.
2. In the root of the project, create a file named `.env`.
3. Add this line to the `.env` file: WEATHER_API_KEY=your_api_key_here
