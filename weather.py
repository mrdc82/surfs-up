import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import geolocations as gl

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": -34.309203125582506,
	"longitude": 18.465065256630176,
	"current": ["temperature_2m", "wind_speed_10m"],
	"wind_speed_unit": "ms"
}
responses = openmeteo.weather_api(url, params=params)
response = responses[0]
# Current values. The order of variables needs to be the same as requested.
current = response.Current()
current_temperature_2m = current.Variables(0).Value()
current_wind_speed_10m = current.Variables(1).Value()

#print(f"Current temperature: {int(current_temperature_2m)}c")
#print(f"Current wind speed: {int(current_wind_speed_10m)}m/s")