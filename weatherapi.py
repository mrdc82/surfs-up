import requests
import json

#asklocation = input("Type weather location: ")
asklocation = "muizenberg"
dow = {1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}

url = f"http://api.weatherapi.com/v1/current.json?key=03e08f13e544491fbb9114121252302&q={asklocation}&aqi=no"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
result = response.json()

#print(json.dumps(result,indent=4))

location = result['location']['name']
region = result['location']['region']
air_temp = result['current']['temp_c']
day = result['current']['is_day']
conditions = result['current']['condition']['text']
wind_speed = result['current']['wind_kph']
wind_direction = result['current']['wind_dir']
wind_chill = result['']
print(wind_direction)
