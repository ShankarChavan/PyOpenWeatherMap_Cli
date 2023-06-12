import requests
from pyopenweathermap_cli.utils import Weather_URL,get_api_key

def greet(user: str) -> str:
    """Greet the user!

    Args:
        user: The name of the user.

    Returns:
        string: A greeting for the user.

    """

    return f"Hello {user}!"

def get_weather(city: str) -> str:
    """Get the weather for a city.

    Args:
        city: The name of the city.

    Returns:
        string: The weather for the city.

    """
    query_url=f"{Weather_URL}?q={city}&appid={get_api_key()}&units=metric"
    response = requests.get(query_url, timeout=5)
    if response.status_code != 200:
        return f"Error getting weather for {city}."
    weather_data = response.json()

    weather = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    
    return f"The weather in {city} is {weather} with a temperature of {temp} degrees Celsius. It feels like {feels_like} degrees Celsius. The humidity is {humidity} percent and the wind speed is {wind_speed} meters per second."
