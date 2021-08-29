from typing import NamedTuple


def get_prime_number():
    """Get a list of prime numbers between x and y."""
    pass

def call_weather_api(url, location):
    """Get the weather of a specific location.
    
    Calling weather API to check for weather by using weather API
    and location. Make sure you provide city name only, country and
    country names won't be accepted and will throw an exception.

    :param url: URL of the weather API
    :type url: str
    :param location: Location of the city to get the weather of.
    :type location: str
    :return: Provide the weather information of a given location.
    :rtype: NamedTuple
    """
    pass

def call_weather_api_with_type(url: str, location: str) -> NamedTuple:
    pass
