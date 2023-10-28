import os
import requests


def get_weather():
  BASE_URL = 'http://api.weatherstack.com/current?'
  my_secret1 = os.environ['API_KEY']
  print(my_secret1)
  url = BASE_URL + "access_key=" + my_secret1 + "&query=" + CITY
  response = requests.get(url).json()
  temperature = response["current"]["temperature"]
  return temperature
