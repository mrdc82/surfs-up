import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import datetime
import geolocations as gl
import condition_locations
import weather

# user is asked for location
ask_location = input("Input location: ")
ask_location = ask_location.lower().replace(' ','_')

latitude = gl.locations[ask_location]['lat']
longitude = gl.locations[ask_location]['lon']
loc_name = ask_location.upper().replace('_', ' ')

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
	"current": ["wave_height", "wave_direction", "wave_period", "wind_wave_direction", "swell_wave_height", "swell_wave_direction", "swell_wave_period"]
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print('\n----------------------------------')
print(f"Coordinates: {response.Latitude():.2f},{response.Longitude():.2f}")
print(f"Location: {loc_name}")

# Current values. The order of variables needs to be the same as requested.
current = response.Current()

current_wave_height = current.Variables(0).Value()

current_wave_direction = current.Variables(1).Value()

current_wave_period = current.Variables(2).Value()

current_wind_wave_direction = current.Variables(3).Value()

current_swell_wave_height = current.Variables(4).Value()

current_swell_wave_direction = current.Variables(5).Value()

current_swell_wave_period = current.Variables(6).Value()

stringtime = datetime.datetime.fromtimestamp(current.Time()).strftime('%Y-%m-%d %H:%M:%S')

# a compass for wind direction
if current_wind_wave_direction in range(0,22):
    curr_wind_direction = "N"
elif current_wind_wave_direction in range(22,67):
    curr_wind_direction = "NE"
elif current_wind_wave_direction in range(67,112):
    curr_wind_direction = "E"
elif current_wind_wave_direction in range(112,157):
    curr_wind_direction = "SE"
elif current_wind_wave_direction in range(157,202):
    curr_wind_direction = "S"
elif current_wind_wave_direction in range(202,247):
    curr_wind_direction = "SW"
elif current_wind_wave_direction in range(247,292):
    curr_wind_direction = "W"
elif current_wind_wave_direction in range(292, 337):
    curr_wind_direction = "NW"

# a compass for swell direction
if current_swell_wave_direction in range(0,22):
    curr_swell_direction = "N"
elif current_swell_wave_direction in range(22,67):
    curr_swell_direction = "NE"
elif current_swell_wave_direction in range(67,112):
    curr_swell_direction = "E"
elif current_swell_wave_direction in range(112,157):
    curr_swell_direction = "SE"
elif current_swell_wave_direction in range(157,202):
    curr_swell_direction = "S"
elif current_swell_wave_direction in range(202,247):
    curr_swell_direction = "SW"
elif current_swell_wave_direction in range(247,292):
    curr_swell_direction = "W"
elif current_swell_wave_direction in range(292, 337):
    curr_swell_direction = "NW"

print(f"Current time: {stringtime}")
print(f"Current wind direction {curr_wind_direction}")
print(f"Current wind speed: {int(weather.current_wind_speed_10m)}m/s")
print(f"Current temperature: {int(weather.current_temperature_2m)}\u2103")
print(f"Current swell height: {current_swell_wave_height:.2f}m")
print(f"Current swell direction: {curr_swell_direction}")
print(f"Current swell period: {int(current_swell_wave_period)}s")
print('----------------------------------\n')

best_spots = "These are your top spots right now"

if curr_wind_direction == "SE":
    print(best_spots + '\n----------------------------------')
    for spot in condition_locations.south_east:
        print(spot)
elif curr_wind_direction == "SW":
    print(condition_locations.south_west)
elif curr_wind_direction == "NE":
    print(condition_locations.north_east)
elif curr_wind_direction == "NW":
    print(condition_locations.north_west)   

print('----------------------------------')