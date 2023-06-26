# PyOpenWeatherMap_Cli
A command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python

# Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

# Features
- [x] Fetch weather data from OpenWeatherMap API
- [x] Parse JSON data using Python
- [x] Display weather data in a readable format
- [x] Accept city name as a command-line argument


# Installation
- Clone this repository
- Install the required packages using the following command:
```bash
poetry install
```


# Usage
- Create an account on [OpenWeatherMap](https://openweathermap.org/) and get your API key
- Clone this repository


Add api_secret to evnironment variable:
```bash
export api_key=<your_api_key>
```

Run the following command to run cli:
```bash
python main.py <command> <city-name>

```
example:
```bash
cd src/pyopenweathermap_cli/
python main.py weather mumbai
```


Output of the above looks like this:
```bash
The weather in Mumbai is drizzle with a temperature of 25.99 degrees Celsius.
It feels like 25.99 degrees Celsius.
The humidity is 100 percent and the wind speed is 1.54 meters per second.
```
