import os
from datetime import datetime

# constants for weather API url and geolocation API url
Weather_URL: str = "https://api.openweathermap.org/data/2.5/weather"


def get_api_key():
    """Read the API key from the environment variable.
    Returns:
        string: The API key.
    """
    api_key_val = os.environ["api_key"]
    return api_key_val


def format_date(timestamp: int) -> str:
    """Formats a timestamp into date time."""
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%m/%d/%Y, %H:%M:%S")
