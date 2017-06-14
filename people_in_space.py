import requests

# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# 3 people are currently in space.
print(data["number"])
print(data)