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
--------------------------------------------------
Location                 : muizenberg
Current time             : 2025-03-20 12:00:00
Current wind direction   : SE
Current wind speed       : 5m/s
Current temperature      : 25℃
Current swell height     : 1.42m
Current swell direction  : S
--------------------------------------------------

+----+----------------+------------------+-------------------+-------------------+-------------------+-------------------+---------------------+----------------+
|    |    Location    |  Wind Direction  |  Wind Speed(m/s)  |  Swell Direction  |  Swell Height(m)  |  Swell Period(s)  |  Water Temperature  |  Distance(km)  |
|----+----------------+------------------+-------------------+-------------------+-------------------+-------------------+---------------------+----------------|
| 22 |   muizenberg   |        SE        |         5         |         S         |       0.94        |         9         |         13          |       0        |
| 27 |  danger beach  |        SE        |         5         |         S         |       0.94        |         9         |         13          |      2.25      |
| 20 |    macassar    |        SE        |         6         |         S         |       0.78        |         9         |         16          |     30.14      |
| 8  |   dias beach   |        SE        |         1         |         S         |       1.44        |         8         |         13          |     32.89      |
| 23 |  pearly beach  |        SE        |         2         |         S         |       1.44        |         8         |         16          |     134.33     |
| 13 | jongensfontein |        SE        |         3         |         S         |       1.34        |         8         |         16          |     321.31     |
| 18 |  skulpiesbaai  |        SE        |         3         |         S         |       1.26        |         8         |         17          |     328.6      |
| 10 | glentana beach |        SE        |         2         |         S         |       1.08        |         8         |         18          |     424.43     |
| 16 | keurboomstrand |        SE        |         3         |         S         |       1.14        |         9         |         17          |     548.76     |
+----+----------------+------------------+-------------------+-------------------+-------------------+-------------------+---------------------+----------------+
Medium swell
------------------------------------
```

## Contributing
Feel free to fork this repository, submit pull requests, or report issues.

## License
This project is licensed under the MIT License.

## Author
Developed by Constantinos (Dino) Charalambous

