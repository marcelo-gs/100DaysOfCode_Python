import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

##Response codes
"""
1XX: Hold On
2XX: Here You Go
3XX: Go Away
4XX: You Screwed Up
5XX: I Screwed Up
"""
#Map Http codes and raise a Exception for http codes
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

##################################################
url = "https://api.sunrise-sunset.org/json"

#Sé - São Paulo - Brazil
latitude = float("-23.551802")
longitude = float("-46.634645")

latitude = float("-23.603918")
longitude = float("-46.799494")

parameters = {
    "lat":latitude,
    "lng":longitude, 
    "formatted": 0
}

response = requests.get(url=url, params=parameters)
data = response.json()["results"]
sunrise = data["sunrise"]
sunset = data['sunset']


