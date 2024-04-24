import requests
import os

appId = os.environ["appId"]
appKey = os.environ["appKey"]
apiEndpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": appId,
    "x-app-key": appKey
}

userInput = input("Tell me which exercises you did: ")
while len(userInput) == 0:
    userInput = input("Invalid, tell me which exercises you did: ")

params = {
    "query": userInput
}

response = requests.post(url=apiEndpoint, params=params, headers=headers)
response.raise_for_status()
print(response)


