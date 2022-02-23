import requests

BASE_URL = "http://127.0.0.1:5000"

response = requests.get(BASE_URL + "/helloworld/lou/25")
print(response.json())