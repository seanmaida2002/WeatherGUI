import requests
from datetime import date
from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.getenv("WEATHER_API_KEY")
API_URL= "http://api.weatherapi.com/v1/forecast.json"



def get_current_weather(city):
    params = {
    "key": API_KEY,
    "q": city,
    "days": "1",
    "aqi": "no",
    "alerts": "no"
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    weather_condition = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_f"]
    picture = data["current"]["condition"]["icon"]
    return {"weather_condition": weather_condition, "temperature": temperature, "picture": picture}

def get_current_date():
    today = date.today()
    formatted_date = today.strftime("%m/%d/%Y")
    return formatted_date