import requests
import json
from os import getenv
from dotenv import load_dotenv

load_dotenv()

myapi_key = getenv('api_key')
asklocation = input("Type weather location: ")
dow = {1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}

url = f"http://api.weatherapi.com/v1/current.json?key={myapi_key}&q={asklocation}&aqi=no"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
result = response.json()

print(json.dumps(result,indent=4))

location = result['location']['name']
region = result['location']['region']
air_temp = result['current']['temp_c']
day = result['current']['is_day']
conditions = result['current']['condition']['text']
wind_speed = result['current']['wind_kph']
wind_direction = result['current']['wind_dir']
wind_chill = result['current']['windchill_c']
wind_gusts = result['current']['gust_kph']
print(wind_gusts)
