import datetime as dt
import requests
import tkinter as tk
from get_api import get_api_key
def get_weather(CITY):
    BASE_URL = 'http://api.weatherstack.com/current?'
    API_KEY = get_api_key()
    url = BASE_URL + "access_key=" +    API_KEY+ "&query=" + CITY
    response = requests.get(url).json()
    temp = response['current']['temperature']
    return temp
