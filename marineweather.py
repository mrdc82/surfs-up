import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import datetime
import geolocations as gl

# user is asked for location
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
	"current": ["wave_height", "wave_direction", "wave_period", "wind_wave_direction", "swell_wave_height", "swell_wave_direction", "swell_wave_period"]
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

current_wind_wave_direction = current.Variables(3).Value()

current_swell_wave_height = current.Variables(4).Value()

current_swell_wave_direction = current.Variables(5).Value()

current_swell_wave_period = current.Variables(6).Value()

mytime = datetime.datetime.fromtimestamp(current.Time()).strftime('%Y-%m-%d %H:%M:%S')

# a compass for wind direction
if current_wind_wave_direction in range(0,22):
    cwvd = "N"
elif current_wind_wave_direction in range(22,67):
    cwvd = "NE"
elif current_wind_wave_direction in range(67,112):
    cwvd = "E"
elif current_wind_wave_direction in range(112,157):
    cwvd = "SE"
elif current_wind_wave_direction in range(157,202):
    cwvd = "S"
elif current_wind_wave_direction in range(202,247):
    cwvd = "SW"
elif current_wind_wave_direction in range(247,292):
    cwvd = "W"
elif current_wind_wave_direction in range(292, 337):
    cwvd = "NW"

# a compass for swell direction
if current_swell_wave_direction in range(0,22):
    cwsd = "N"
elif current_swell_wave_direction in range(22,67):
    cwsd = "NE"
elif current_swell_wave_direction in range(67,112):
    cwsd = "E"
elif current_swell_wave_direction in range(112,157):
    cwsd = "SE"
elif current_swell_wave_direction in range(157,202):
    cwsd = "S"
elif current_swell_wave_direction in range(202,247):
    cwsd = "SW"
elif current_swell_wave_direction in range(247,292):
    cwsd = "W"
elif current_swell_wave_direction in range(292, 337):
    cwsd = "NW"

print(f"Current time: {mytime}")
print(f"Current wave_height: {current_wave_height}")
print(f"Current wave_direction: {current_wave_direction}")
print(f"Current wave_period: {current_wave_period}")
print(f"Current wind_wave_direction {cwvd}")
print(f"Current swell_wave_height: {current_swell_wave_height}")
print(f"Current swell_wave_direction: {cwsd}")
print(f"Current swell_wave_period: {current_swell_wave_period}")