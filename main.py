import requests
import time as sleep

api_key = "write a api key "
base_url = "get the use  website url "
city_name = input("Enter city name: ")


complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
print(response)
data = response.json()
print(data)

if data["cod"] != "404":
    # Getting the weather information
     weather = data["weather"][0]["description"]
     temperature = data["main"]["temp"]
     feells = data["main"]["feels_like"]   # hissedilen
     humidity = data["main"]["humidity"]
     wind_speed = data["wind"]["speed"]
     syss = data["sys"]["country"]

    # Converting temperature from Kelvin to Celsius
temperature_celsius = temperature - 273.15

    # Printing the weather information
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature_celsius:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"feells:{feells} tahmini")
    # print(f"ülke": {syss}.capitalize()")
    else:
    print("City not found")

    if data["cod"] != "404":
        print("This system doesn`t work")

