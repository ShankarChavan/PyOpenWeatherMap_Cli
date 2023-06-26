from dataclasses import asdict, dataclass

import requests
from rich import print

from pyopenweathermap_cli.utils import Weather_URL, format_date, get_api_key


@dataclass
class WeatherInfo:
    """Stores weather information."""

    city: str
    temp: float
    desc: str
    feels_like: float
    humidity: int
    wind_speed: float

    @classmethod
    def from_dict(cls, data: dict) -> "WeatherInfo":
        return cls(
            city=data["name"],
            temp=data["main"]["temp"],
            desc=data["weather"][0]["description"],
            feels_like=data["main"]["feels_like"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
        )


def get_weather(city: str) -> dict:
    """Get the weather for a city.
    Args:
        city: The name of the city.
    Returns:
        string: The weather for the city.
    """

    query_url = f"{Weather_URL}?q={city}&appid={get_api_key()}&units=metric"

    response = requests.get(query_url, timeout=5)

    if response.status_code != 200:
        return f"Error getting weather for {city}."

    weather_data = response.json()
    weather_info = WeatherInfo.from_dict(weather_data)
    return weather_info


def print_weather_info(data: WeatherInfo) -> str:
    """Prints the weather information.
    Args:
        data: The weather information.
    """
    city = data.city
    weather = data.desc
    temp = data.temp
    feels_like = data.feels_like
    humidity = data.humidity
    wind_speed = data.wind_speed

    print(
        f"The weather in [green]{city}[/green] is [green]{weather}[/green] with a temperature of [green]{temp}[/green] degrees Celsius.\nIt feels like [green]{feels_like}[/green] degrees Celsius.\nThe humidity is [green]{humidity}[/green] percent and the wind speed is [green]{wind_speed}[/green] meters per second."
    )
