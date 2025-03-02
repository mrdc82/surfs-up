import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import datetime
import geolocations as gl
import condition_locations
import location_data
from pprint import pprint
import numpy as np


# Some print stuff for cleanliness
dashes = "-"

# user is asked for location
ask_location = input("Input location: ")
#ask_location = "cape town"
ask_location = ask_location.lower().replace(' ','_')

latitude = gl.locations[ask_location]['lat']
longitude = gl.locations[ask_location]['lon']
loc_name = ask_location.capitalize().replace('_', ' ')

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def get_weather():
    global weather_current_wind_speed_10m
    global weather_current_temperature_2m
    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": {latitude},
        "longitude": {longitude},
        "current": ["temperature_2m", "wind_speed_10m"],
        "wind_speed_unit": "ms"
    }
    weather_responses = openmeteo.weather_api(weather_url, params=weather_params)
    weather_response = weather_responses[0]
    # Current values. The order of variables needs to be the same as requested.
    weather_current = weather_response.Current()
    weather_current_temperature_2m = int(weather_current.Variables(0).Value())
    weather_current_wind_speed_10m = int(weather_current.Variables(1).Value() * 2)

def get_marine_data():
    global current_swell_wave_height
    global current_swell_wave_period
    global current_sea_surface_temperature
    global current_wind_wave_direction
    global current_swell_wave_direction
    global stringtime

    url = "https://marine-api.open-meteo.com/v1/marine"
    params = {
        "latitude": {latitude},
        "longitude": {longitude},
        "current": ["wave_height", "wave_direction", "wave_period", "wind_wave_direction", 
                "swell_wave_height", "swell_wave_direction", "swell_wave_period", "sea_surface_temperature"]
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    #print('\n----------------------------------')
    #print(f"Coordinates: {response.Latitude():.2f},{response.Longitude():.2f}")
    #print(f"Location: {loc_name}")

    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()
    current_wave_height = int(current.Variables(0).Value())
    current_wave_direction = int(current.Variables(1).Value())
    current_wave_period = int(current.Variables(2).Value())
    current_wind_wave_direction = int(current.Variables(3).Value())
    current_swell_wave_height = round((current.Variables(4).Value() * 2), 2)
    current_swell_wave_direction = int(current.Variables(5).Value())
    current_swell_wave_period = int(current.Variables(6).Value())
    current_sea_surface_temperature = int(current.Variables(7).Value())
    stringtime = datetime.datetime.fromtimestamp(current.Time()).strftime('%Y-%m-%d %H:%M:%S')

# Iterate through all locations
# Add data entries to table in location_data module
'''for l in gl.locations:
    latitude = gl.locations[l]['lat']
    longitude = gl.locations[l]['lon']
    loc_name = l.capitalize().replace('_', ' ')
    get_weather()
    get_marine_data()
    location_data.add_entry(loc_name, weather_current_wind_speed_10m, current_swell_wave_height,
                            current_swell_wave_period, current_sea_surface_temperature)
'''
#pprint(location_data.table)

get_weather()
get_marine_data()

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
print(f"Current wind speed: {int(weather_current_wind_speed_10m)}m/s")
print(f"Current temperature: {int(weather_current_temperature_2m)}\u2103")
print(f"Current swell height: {current_swell_wave_height:.2f}m")
print(f"Current swell direction: {curr_swell_direction}")
print(f"Current swell period: {int(current_swell_wave_period)}s")
print(f"Current water temperature: {int(current_sea_surface_temperature)}\u2103")
print('----------------------------------\n')

# Only applies to swell size as wind will have very little effect. Swell must be over 0.5m.
if weather_current_wind_speed_10m < 5 and current_swell_wave_height > 0.5:
    if curr_swell_direction == "SE": 
        for spot in condition_locations.north_west:
            print(spot)
    elif curr_swell_direction == "SW":
        for spot in condition_locations.north_east:
            print(spot)
    elif curr_swell_direction == "NE":
        for spot in condition_locations.south_west:
            print(spot)
    elif curr_wind_direction == "NW":
        for spot in condition_locations.south_east:
            print(spot)
    elif curr_wind_direction == "S":
        for spot in condition_locations.north:
            print(spot)
    elif curr_wind_direction == "N":
        for spot in condition_locations.south:
            print(spot)
    elif curr_wind_direction == "E":
        for spot in condition_locations.west:
            print(spot)
    elif curr_wind_direction == "W":
        for spot in condition_locations.east:
            print(spot)
    else:
        pass

def wind_and_swell():
    if curr_wind_direction == "SE" and curr_swell_direction == "NW":
        for spot in condition_locations.south_east:
            print(spot)
    elif curr_wind_direction == "SW" and curr_swell_direction == "NE":
        for spot in condition_locations.south_west:
            print(spot)
    elif curr_wind_direction == "NE" and curr_swell_direction == "SW":
        for spot in condition_locations.north_east:
            print(spot)
    elif curr_wind_direction == "NW" and curr_swell_direction == "SE":
        for spot in condition_locations.north_west:
            print(spot)
    elif curr_wind_direction == "S" and (curr_swell_direction == "NE" or curr_swell_direction == "NW" or curr_swell_direction == "N"):
        for spot in condition_locations.south_desc:
            print(spot)
    elif curr_wind_direction == "N" and (curr_swell_direction == "SE" or curr_swell_direction == "SW" or curr_swell_direction == "S"):
        for spot in condition_locations.north_desc:
            print(spot)
    elif curr_wind_direction == "E" and (curr_swell_direction == "NW" or curr_swell_direction == "SW" or curr_swell_direction == "W"):
        for spot in condition_locations.east_desc:
            print(spot)
    elif curr_wind_direction == "W" and (curr_swell_direction == "NE" or curr_swell_direction == "SE" or curr_swell_direction == "E"):
        for spot in condition_locations.west_desc:
            print(spot)
    else:
        pass

# List comprehension for swell heights represented in floats.
swell_beginners = [float(round(sb, 10)) for sb in np.arange(0.5,1.3,0.01)]
swell_intermediate = [float(round(sb, 10)) for sb in np.arange(1.2,2.6,0.01)]
swell_advanced = [float(round(sb, 10)) for sb in np.arange(2.5,4.0,0.01)]

if wind_and_swell():
    if current_swell_wave_height in swell_beginners and weather_current_wind_speed_10m < 5 and current_swell_wave_period in range(5,10):
        print(f"Easy long board sessions, great for beginners\n{dashes*45}")
    elif current_swell_wave_height in swell_intermediate and weather_current_wind_speed_10m in range(0,8) and current_swell_wave_period in range(5,15):
        print(f"Some good surfing out there, get stuck in\n{dashes*41}")
    elif current_swell_wave_height in swell_advanced and weather_current_wind_speed_10m in range(0,10) and current_swell_wave_period > 10:
        print(f"These are next level conditions, beefcake stuff, beginners need not respond!\n{dashes*76}")
else:
    print(f"\n{dashes*29}\nFlatter than a pancake my bru\n{dashes*29}")