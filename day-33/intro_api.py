import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# print(response.status_code)
iss_data = response.json()
print(iss_data)

latitude = iss_data["iss_position"]["latitude"]
longitude = iss_data["iss_position"]["longitude"]

# you can specify what key you are ONLY interested with this syntax
# data = response.json["iss_position"]
# can go even further like
# data = response.json["iss_position"]["longitude"]
# data = response.json()

params = {
    "lat": float(latitude),
    "lng": float(longitude),
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
# throws error if status code != 200
response.raise_for_status()
sun_data = response.json()
print(sun_data)
