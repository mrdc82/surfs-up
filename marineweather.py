import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import datetime
import geolocations as gl



ask_location = input("Input location: ")

if ask_location == 'muizenberg':
    latitude = gl.locations['muizenberg']['lat']
    longitude = gl.locations['muizenberg']['lon']
    loc_name = ask_location.upper()
elif ask_location == 'black rock':
    latitude = gl.locations['black_rock']['lat']
    longitude = gl.locations['black_rock']['lon']
    loc_name = ask_location.upper()
else:
    print('Location does not exist')



# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://marine-api.open-meteo.com/v1/marine"
params = {
	"latitude": {latitude},
	"longitude": {longitude},
	"current": ["wave_height", "wave_direction", "wave_period", "swell_wave_height", "swell_wave_direction", "swell_wave_period"]
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates: {response.Latitude()} {response.Longitude()}")
print(f"Location: {loc_name}")
#print(f"Elevation {response.Elevation()} m asl")
#print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
#print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Current values. The order of variables needs to be the same as requested.
current = response.Current()

current_wave_height = current.Variables(0).Value()

current_wave_direction = current.Variables(1).Value()

current_wave_period = current.Variables(2).Value()

current_swell_wave_height = current.Variables(3).Value()

current_swell_wave_direction = current.Variables(4).Value()

current_swell_wave_period = current.Variables(5).Value()

mytime = datetime.datetime.fromtimestamp(current.Time()).strftime('%Y-%m-%d %H:%M:%S')

print(f"Current time: {mytime}")
print(f"Current wave_height: {current_wave_height}")
print(f"Current wave_direction: {current_wave_direction}")
print(f"Current wave_period: {current_wave_period}")
print(f"Current swell_wave_height: {current_swell_wave_height}")
print(f"Current swell_wave_direction: {current_swell_wave_direction}")
print(f"Current swell_wave_period: {current_swell_wave_period}")