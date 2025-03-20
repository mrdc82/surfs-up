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
import compass
from tabulate import tabulate

# Some print stuff for cleanliness
dashes = "-"

global top_spots
top_spots = []

# user is asked for location
'''ask_location = input("Input location: ")
ask_location = "cape town"
ask_location = ask_location.lower().replace(' ','_')

latitude = gl.locations[ask_location]['lat']
longitude = gl.locations[ask_location]['lon']
loc_name = ask_location.capitalize().replace('_', ' ')
'''

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
    weather_current_wind_speed_10m = int(weather_current.Variables(1).Value() * 1.5)

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
    response = responses[0]

    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()
    current_wave_height = int(current.Variables(0).Value())
    current_wave_direction = int(current.Variables(1).Value())
    current_wave_period = int(current.Variables(2).Value())
    current_wind_wave_direction = int(current.Variables(3).Value())
    current_swell_wave_height = round((current.Variables(4).Value()), 2)
    current_swell_wave_direction = int(current.Variables(5).Value())
    current_swell_wave_period = int(current.Variables(6).Value())
    current_sea_surface_temperature = int(current.Variables(7).Value())
    stringtime = datetime.datetime.fromtimestamp(current.Time()).strftime('%Y-%m-%d %H:%M:%S')

# Iterate through all locations from geolocations.py
# Adding data entries to table in location_data.py
for l in gl.locations:
    latitude = gl.locations[l]['lat']
    longitude = gl.locations[l]['lon']
    get_weather()
    get_marine_data()
    location_data.add_entry(l, compass.curr_wind_direction, weather_current_wind_speed_10m, compass.curr_swell_direction, current_swell_wave_height,
                            current_swell_wave_period, current_sea_surface_temperature)

# Convert list to NumPy array then panda dataframe
np_table = np.array(location_data.table, dtype=object)
df = pd.DataFrame(location_data.table, columns=["Location",
                                                "Wind Direction",
                                                "Wind Speed(m/s)",
                                                "Swell Direction",
                                                "Swell Height(m)",
                                                "Swell Period(s)",
                                                "Water Temperature"])

print(f'{dashes*50}')
print("Location                 : Cape Town")
print(f"Current time             : {stringtime}")
print(f"Current wind direction   : {compass.curr_wind_direction}")
print(f"Current wind speed       : {int(weather_current_wind_speed_10m)}m/s")
print(f"Current temperature      : {int(weather_current_temperature_2m)}\u2103")
print(f"Current swell height     : {current_swell_wave_height:.2f}m")
print(f"Current swell direction  : {compass.curr_swell_direction}")
#print(f"Current swell period     : {int(current_swell_wave_period)}s")
#print(f"Current water temperature: {int(current_sea_surface_temperature)}\u2103")
print(f'{dashes*50}\n')

# List comprehension for swell heights represented in floats.
swell_beginners = [float(round(sb, 10)) for sb in np.arange(0.5,1.3,0.01)]
swell_intermediate = [float(round(sb, 10)) for sb in np.arange(1.2,2.6,0.01)]
swell_advanced = [float(round(sb, 10)) for sb in np.arange(2.5,6.0,0.01)]
same_wind_swell = "Conditions likely flat if very strong winds are relatively in the same direction as swell"

# Only applies to swell size as wind will have very little effect. Swell must be over 0.5m.
def swell_no_wind():
    if weather_current_wind_speed_10m < 5:
        if (compass.curr_swell_direction == "SE"):
            for spot in condition_locations.north_west:
                top_spots.append(spot)
        elif compass.curr_swell_direction == "SW":
            for spot in condition_locations.north_east:
                top_spots.append(spot)
        elif compass.curr_swell_direction == "NE":
            for spot in condition_locations.south_west:
                top_spots.append(spot)
        elif compass.curr_swell_direction == "NW":
            for spot in condition_locations.south_east:
                top_spots.append(spot)
        elif compass.curr_swell_direction == "S":
            for spot in condition_locations.north:
                top_spots.append(spot)
        elif compass.curr_swell_direction == "N":
            for spot in condition_locations.south:
                top_spots.append(spot)
        elif compass.curr_swell_direction == "E":
            for spot in condition_locations.west:
                top_spots.append(spot)
        elif compass.curr_swell_direction == "W":
            for spot in condition_locations.east:
                top_spots.append(spot)
        else:
            pass

def wind_and_swell():
    if weather_current_wind_speed_10m > 5:
        if (compass.curr_wind_direction == "SE") and (compass.curr_swell_direction == "NW"): # SE Wind
            for spot in condition_locations.south_east:
                top_spots.append(spot)
        elif (compass.curr_wind_direction == "SW") and (compass.curr_swell_direction == "NE"): # SW Wind
            for spot in condition_locations.south_west:
                top_spots.append(spot)
        elif (compass.curr_wind_direction == "NE") and (compass.curr_swell_direction == "SW"): # NE Wind
            for spot in condition_locations.north_east:
                top_spots.append(spot)
        elif (compass.curr_wind_direction == "NW") and (compass.curr_swell_direction == "SE"): # NW Wind
            for spot in condition_locations.north_west:
                top_spots.append(spot)
        elif (compass.curr_wind_direction == "S") and (compass.curr_swell_direction == "N"): # South
            for spot in condition_locations.south:
                top_spots.append(spot)
        elif (compass.curr_wind_direction == "N") and (compass.curr_swell_direction == "S"): # North
            for spot in condition_locations.north:
                top_spots.append(spot)
        elif (compass.curr_wind_direction == "E") and (compass.curr_swell_direction == "W"): # East
            for spot in condition_locations.east:
                top_spots.append(spot)
        elif (compass.curr_wind_direction == "W") and (compass.curr_swell_direction == "E"): # West
            for spot in condition_locations.west:
                top_spots.append(spot)
        else:
            pass

def same_wind_and_swell():  # where wind is strong and swell is in the same or cross direction as the wind
    if weather_current_wind_speed_10m > 7:
        if compass.curr_wind_direction == compass.curr_swell_direction:
            print(f"{dashes*89}\n{same_wind_swell}")
        else:
            print(f"{dashes*89}\n{same_wind_swell}")

wind_and_swell()
swell_no_wind()
same_wind_and_swell()

#Output the data of the best found locations in a panda dataframe.
if len(top_spots) > 0:
    mask = df['Location'].isin(top_spots)
    active_spots = df[mask]
    print(tabulate(active_spots, headers = 'keys', tablefmt = 'psql', numalign='center', stralign='center'))
else:
    pass

#Determine surfing conditions based on swell size and wind direction
if current_swell_wave_height in swell_beginners:
    print(f"Small swell\n{dashes*33}")
elif current_swell_wave_height in swell_intermediate:
    print(f"Medium swell\n{dashes*36}")
elif current_swell_wave_height in swell_advanced:
    print(f"Large swells, proceed with caution\n{dashes*34}")
else:
    print(f"\n{dashes*52}\nQuestionable, check cams or reports for more details\n{dashes*52}")

