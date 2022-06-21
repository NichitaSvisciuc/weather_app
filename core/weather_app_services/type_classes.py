from dataclasses import dataclass
from typing import NamedTuple


class ApiWeatherResponse(NamedTuple):
	location : str
	condition : str
	wind_dir : str
	humidity : float
	temperature : int
	feels_like : int
	wind_kph : float
	days : list


class DateTimeResponse(NamedTuple):
	day_name : str
	month_name : str
	day : int