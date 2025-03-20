# This is a compass

import openmeteo_requests
import requests_cache
from retry_requests import retry
import geolocations as gl

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

base = input('What is your current location? ')
#base = 'muizenberg'
base_coordinates = gl.locations[base]

url = "https://marine-api.open-meteo.com/v1/marine"
params = {
    "latitude": base_coordinates['lat'],
    "longitude": base_coordinates['lon'],
    "current": ["wind_wave_direction", "swell_wave_direction"]
}
responses = openmeteo.weather_api(url, params=params)
response = responses[0]
current = response.Current()
response = responses[0]
current_wind_wave_direction = int(current.Variables(0).Value())
current_swell_wave_direction = int(current.Variables(1).Value())

# a compass for wind direction
if current_wind_wave_direction in range(0,19) or current_wind_wave_direction in range(351,360):
    curr_wind_direction = "N"
elif current_wind_wave_direction in range(20,70,1):
    curr_wind_direction = "NE"
elif current_wind_wave_direction in range(90,134,1):
    curr_wind_direction = "E"
elif current_wind_wave_direction in range(135,179,1):
    curr_wind_direction = "SE"
elif current_wind_wave_direction in range(180,224,1):
    curr_wind_direction = "S"
elif current_wind_wave_direction in range(225,269,1):
    curr_wind_direction = "SW"
elif current_wind_wave_direction in range(270,314,1):
    curr_wind_direction = "W"
elif current_wind_wave_direction in range(315,350,1):
    curr_wind_direction = "NW"

# a compass for swell direction
if current_swell_wave_direction in range(0,19) or current_swell_wave_direction in range(351,360):
    curr_swell_direction = "N"
elif current_swell_wave_direction in range(20,70,1):
    curr_swell_direction = "NE"
elif current_swell_wave_direction in range(90,134,1):
    curr_swell_direction = "E"
elif current_swell_wave_direction in range(135,179,1):
    curr_swell_direction = "SE"
elif current_swell_wave_direction in range(180,224,1):
    curr_swell_direction = "S"
elif current_swell_wave_direction in range(225,269,1):
    curr_swell_direction = "SW"
elif current_swell_wave_direction in range(270,314,1):
    curr_swell_direction = "W"
elif current_swell_wave_direction in range(315,350,1):
    curr_swell_direction = "NW"