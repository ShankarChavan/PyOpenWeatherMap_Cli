# PyOpenWeatherMap_Cli
A command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python

# Features
- [x] Fetch weather data from OpenWeatherMap API
- [x] Parse JSON data using Python
- [x] Display weather data in a readable format
- [x] Accept city name as a command-line argument

# Usage
- Create an account on [OpenWeatherMap](https://openweathermap.org/) and get your API key
- Clone this repository
- Create a file named `secrets.ini` in the root directory of the project

- Open terminal and run the following command:
```bash
touch secrets.ini
```

Add secret key to the `secrets.ini` file in the following format:
```ini
; secrets.ini
[openweather]
api_key=<YOUR-OPENWEATHER-API-KEY>
```

Run the following command to run cli:
```bash
python3 main.py <city-name>
```




