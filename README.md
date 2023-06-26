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


Add api_secret to evnironment variable:
```bash
export api_key=<your_api_key>
```

Run the following command to run cli:
```bash
python main.py weather <city-name>
```
