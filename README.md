# Surf Weather App

## Overview
The **Surf Weather App** is a Python-based application that gathers real-time weather data from [WeatherAPI.com](https://www.weatherapi.com/) and [Open-Meteo.com](https://open-meteo.com/) to determine the best surfing conditions in various locations around the Western Cape, South Africa. When optimal surf conditions are met, the app displays all locations that currently offer the best waves for surfing.

## Features
- Fetches live weather data using the `weatherapi.com` API.
- Collects marine weather data such as swell height, direction, and period from `open-meteo.com`.
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
1. Obtain an API key from [WeatherAPI.com](https://www.weatherapi.com/) if needed.
2. Save the API key in a `.env` file or modify `weatherapi.py` to include it.
3. Run the scripts:
   ```sh
   python weatherapi.py
   ```
   ```sh
   python marineweather.py
   ```
4. `weatherapi.py` fetches general weather data, while `marineweather.py` collects marine-specific conditions.
5. The scripts will fetch the weather data and display the best surf locations based on predefined criteria.

## Configuration
You can modify the criteria for optimal surf conditions in `weatherapi.py` and `marineweather.py`, such as:
- Wind direction
- Swell height
- Swell period
- Wave consistency

Ensure the `.env` file contains:
```
API_KEY=your_api_key_here
```

The scripts also require the following imports:
```python
import json
from os import getenv
from dotenv import load_dotenv
```

## Example Output
```
Fetching weather data...
Fetching marine weather data...
Best surf spots right now:
- Muizenberg: 3m swell, offshore wind
- Big Bay: 2.5m swell, cross-shore wind
```

## Contributing
Feel free to fork this repository, submit pull requests, or report issues.

## License
This project is licensed under the MIT License.

## Author
Developed by Constantinos (Dino) Charalambous

