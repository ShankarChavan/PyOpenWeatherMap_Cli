from configparser import ConfigParser

#constants for weather API url and geolocation API url
Weather_URL:str = "https://api.openweathermap.org/data/2.5/weather"
Geolocation_URL:str  = "http://api.openweathermap.org/geo/1.0/direct"


# write get_api_key() function to read api key from secrets.ini file
def get_api_key():
    """Read the API key from the secrets.ini file.

    Returns:
        string: The API key.

    """
    config = ConfigParser()
    config.read("../../secrets.ini")
    return config["openweathermap"]["api_key"]
