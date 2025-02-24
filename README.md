# Surf Weather App

## Overview
The **Surf Weather App** is a Python-based application that gathers real-time weather data from [Open-Meteo.com](https://open-meteo.com/) to determine the best surfing conditions in various locations around the Western Cape, South Africa. When optimal surf conditions are met, the app displays all locations that currently offer the best waves for surfing.

## Features
- Fetches live weather data using the `open-meteo.com` API.
- Collects marine and weather data such as swell height, direction, and period from `open-meteo.com`.
- Analyzes surf conditions based on key weather parameters.
- Compares conditions at multiple surf locations in the Western Cape.
- Displays a list of the best surf spots at the time of execution.

## Prerequisites
Before running the application, ensure you have the following installed:

- Python 3.x
- `requests` library

Install dependencies using:
```sh
pip install openmeteo-requests
pip install requests-cache retry-requests numpy pandas
pip install python-dotenv
```

## Usage
1. Open-Meteo does not make use of an API Key for non-commercial use, but is limited to less than 10,000 requests per day.
2. Run the scripts:
   ```sh
   python marineweather.py
   ```
3. `marineweather.py` collects marine-specific conditions.
4. The script will fetch the weather data and display the best surf locations based on predefined criteria.
5. The script makes calls to `condition_locations.py` and `geolocations.py` modules for co-ordinates and location names.

## Configuration
You can modify the criteria for optimal surf conditions in `marineweather.py`, such as:
- Wind direction
- Swell height
- Swell period
- Wave consistency

If you take a non-commercial license, ensure the `.env` file contains:
```
API_KEY=your_api_key_here
```

The scripts requires the following imports:
```sh
pip install -r requirements.txt
```

## Example Output
```
----------------------------------
Coordinates: -34.29,18.46
Location: BLACK ROCK
Current time: 2025-02-24 17:00:00
Current wind direction S
Current wind speed: 7m/s
Current temperature: 22℃
Current swell height: 2.22m
Current swell direction: SW
Current swell period: 9s
Current water temperature: 13℃
----------------------------------

These are your best spots based on wind conditions only.
You'll need to check online for more details
---------------------------------------------------------
Llandudno (beautiful beach, heavy waves)
Dungeons (Hout Bay) (big wave spot)
Outer Kom / Inner Kom (great left-hand point break)
Misty Cliffs (fun for barrels)
Scarborough (powerful beach break)
Long Beach (Kommetjie) (best for all skill levels, clean waves)
```

## Contributing
Feel free to fork this repository, submit pull requests, or report issues.

## License
This project is licensed under the MIT License.

## Author
Developed by Constantinos (Dino) Charalambous

