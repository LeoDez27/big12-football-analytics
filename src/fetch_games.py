import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CFBD_API_KEY")

url = "https://api.collegefootballdata.com/games"

headers = {
    "Authorization": f"Bearer {api_key}"
}

params = {
    "year": 2023,
    "conference": "B12"
}

response = requests.get(url, headers=headers, params=params)

print ("Status code:", response.status_code)

data = response.json()
print( "Number of games:", len(data))
print(data[0]["homeTeam"], "vs", data[0]["awayTeam"], "-", data[0]["homePoints"], "-", data[0]["awayPoints"])

