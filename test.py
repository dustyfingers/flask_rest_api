import requests

BASE_URL = "http://127.0.0.1:5000"

response = requests.get(BASE_URL + "/videos/123")

print(response.json())

response = requests.put(BASE_URL + "/videos/456", { "likes": 100 })

print(response.json())