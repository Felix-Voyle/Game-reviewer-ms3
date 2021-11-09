import requests
import json


parameters = {
    "page_size": 12,
    "search": "Cyberpunk"
}

response = requests.get(f"https://api.rawg.io/api/games?key=2bd342655e2945bc9e97632d8f34bb91", params=parameters)
data = response.json()

with open('data.json', 'w') as f:
    json.dump(data, f)
