# This module contains lists that are populated from the main script
# to reference back to in the results.

import numpy as np

table = []  # This will act as your table

def add_entry(loc_name, curr_wind_direction, weather_current_wind_speed_10m, curr_swell_direction, current_swell_wave_height,
                        current_swell_wave_period, current_sea_surface_temperature, distance):
    """Function to add a new row to the table."""
    table.append({
        "Location": loc_name, 
        "Wind Direction": curr_wind_direction, 
        "Wind Speed(m/s)": weather_current_wind_speed_10m, 
        "Swell Direction": curr_swell_direction, 
        "Swell Height(m)": current_swell_wave_height, 
        "Swell Period(s)": current_swell_wave_period,
        "Water Temperature": current_sea_surface_temperature,
        "Distance(km)": distance
        })