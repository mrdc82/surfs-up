# Surf Weather App

## Overview
The **Surf Weather App** is a Python-based application that gathers real-time weather data from [WeatherAPI.com](https://www.weatherapi.com/) to determine the best surfing conditions in various locations around the Western Cape, South Africa. When optimal surf conditions are met, the app displays all locations that currently offer the best waves for surfing.

## Features
- Fetches live weather data using the `weatherapi.com` API.
- Analyzes surf conditions based on key weather parameters.
- Compares conditions at multiple surf locations in the Western Cape.
- Displays a list of the best surf spots at the time of execution.

## Prerequisites
Before running the application, ensure you have the following installed:

- Python 3.x
- `requests` library

Install dependencies using:
```sh
pip install requests
```

## Usage
1. Obtain an API key from [WeatherAPI.com](https://www.weatherapi.com/).
2. Save the API key in a `.env` file or modify `weatherapi.py` to include it.
3. Run the script:
   ```sh
   python weatherapi.py
   ```
4. The script will fetch the weather data and display the best surf locations based on predefined criteria.

## Configuration
You can modify the criteria for optimal surf conditions in `weatherapi.py`, such as:
- Wind direction
- Swell height
- Swell period
- Wave consistency

## Example Output
```
Fetching weather data...
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

