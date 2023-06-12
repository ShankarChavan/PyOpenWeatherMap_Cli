from typing import Union
import requests
from pyopenweathermap_cli.utils import Geolocation_URL,get_api_key


def get_coordinates(city:str)->Union[float,float]:

    """Get the coordinates of a city.

    Args:
        city: The name of the city.

    Returns:
        tuple: The latitude and longitude of the city.

    """
    query_url=f"{Geolocation_URL}?q={city}&limit=1&appid={get_api_key()}"
    response = requests.get(query_url, timeout=5)
    
    if response.status_code != 200:
        return f"Error getting geolocation for {city}."
    geolocation_data = response.json()
    latitude = geolocation_data[0]["lat"]
    longitude = geolocation_data[0]["lon"]
    return latitude,longitude
