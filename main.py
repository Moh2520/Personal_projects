import datetime as dt
import requests

BASE_URL= "http://api.openweathermap.org/data/2.5/weather?"
API_KEY =  "5d27282396cf771bd807f4a2b30aa045"
CITY= "New York"

def kelvin_to_celsius_farenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit



url = BASE_URL + "appid=" + API_KEY +"&q=" + CITY
response = requests.get(url).json()



temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_farenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_farenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f"Temperature in {CITY}: {temp_celsius:.2f}degrees C or {temp_fahrenheit} degrees F")
print(f"Temperature in {CITY}: feels like: {feels_like_celsius:.2f}degrees C or {feels_like_fahrenheit} degrees F")
print(f"humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"Genaral Weather in {CITY}: {description}")
print(f"sunrise in {CITY} at {sunrise_time} local time.")
print(f"sunset in {CITY} at {sunset_time} local time.")
