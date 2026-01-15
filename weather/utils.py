import requests
import logging
from django.conf import settings


logger = logging.getLogger(__name__)

def fetch_weather_data(city,aqi= 'no'):
    """
    Fetch weather data for a given external weather API.

    Args:
        city(str): The name of the city to fetch weather data for.
    Returns:
        dict: A dictionary containing weather data if the request is successful
    """

    api_key = settings.WEATHER_API_KEY
    base_url = "http://api.weatherapi.com/v1/current.json"
    params={
        'key': api_key,
        'q': city,
        'aqi': aqi,
    }


    try:


        # ten seconds timeout for the request
        response = requests.get(base_url,params=params,timeout=10)
        # raise an error for bad responses (4xx and 5xx)
        response.raise_for_status()  

        return response.json(),response.status_code
    
    except requests.exceptions.Timeout:
        logger.error(f"request to weather API timed out for city : {city}")
        return{"error": "requests timed out"}, 504
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occured : {http_err} for city : {city}")
        return{"error": str(http_err)},response.status_code if 'response' in locals else 504
    
    except Exception as err:
        logger.error(f"An error occured: {err} for city : {city}")
        return{"error": "anb unexpected error occured"}, 500