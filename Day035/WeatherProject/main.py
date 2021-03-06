import requests

#Api Key
API_KEY = "OpenWeatherAPIKEY"
MY_LAT = -23.603918 # Your latitude
MY_LONG = -46.799494 # Your longitude

#Sp, Zona Leste
MY_LAT = -23.577695 # Your latitude
MY_LONG = -46.484849 # Your longitude

URL = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": "metric",
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][0:12]
will_rain = False

for hour_data in weather_slice:
    print(hour_data["weather"][0])
    if hour_data["weather"][0]["id"] > 700:
        will_rain = True

if will_rain:
    print(weather_data["alerts"])
    print("Bring an Umbrella")
    #send an e-mail or text someone
    #fell free to do anything