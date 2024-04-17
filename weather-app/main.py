import requests
import os
from twilio.rest import Client
def checkForRain():
    for list in weather_data["list"]:
        for item in list["weather"]:
            if item["id"] < 700:
                print("is going to rain")
                return True
    print("No rain")
    return False

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
api_key = os.environ["api_key"]
twilio_number = os.environ["twilio_number"]
my_number = os.environ["my_number"]
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
latitude = "33.684566"
longitude = "-117.826508"
rain_lat = 31.918240
rain_long = 131.418380
count = 4

params = {
    "lat": rain_lat,
    "lon": rain_long,
    "appid": api_key,
    "cnt": count
}
response = requests.get(url=api_endpoint, params=params)
response.raise_for_status()
weather_data = response.json()

if checkForRain():
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body="Bring an umbrella",
        from_=twilio_number,
        to=my_number
    )
else:
    print("All good no umbrella needed")

print("End")