import requests
import json

from .type_classes import ApiWeatherResponse

from django.conf import settings

def search_weather_api_by_location(location : str) -> ApiWeatherResponse:

	weather_api_key = settings.WEATHER_SERVICE_API_KEY
	
	request_weather = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={location}&days=7&aqi=no&alerts=no')

	request_weather_dict = json.loads(request_weather.text)

	return ApiWeatherResponse(
			location = request_weather_dict['location']['name'],
			condition = request_weather_dict['current']['condition']['text'],
			wind_dir = request_weather_dict['current']['wind_dir'],
			humidity = int(request_weather_dict['current']['humidity']),
			temperature = int(request_weather_dict['current']['temp_c']),
			feels_like = int(request_weather_dict['current']['feelslike_c']),
			wind_kph = float(request_weather_dict['current']['wind_kph']),
			days = list(request_weather_dict['forecast']['forecastday']),
		)