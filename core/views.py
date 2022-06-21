from django.views.generic import TemplateView
from django.views import View

from django.shortcuts import render, redirect

from .weather_app_services.type_classes import ApiWeatherResponse, DateTimeResponse
from .weather_app_services.api_calls import search_weather_api_by_location

from subscriptions.models import Subscription

import datetime
import calendar
import geocoder


class MainPage(View):

	template_name = 'index.html'

	def get(self, request, **kwargs):

		weather_status = ApiWeatherResponse(
							location = 'You did not requested any location',
							condition = '0',
							wind_dir = 'None',
							humidity = 0.0,
							temperature = 0.0,
							feels_like = 0.0,
							wind_kph = 0.0,
							days = ['']
						)

		searched_location = request.GET.get('search-bar-text', '')

		if searched_location != '':
			weather_status = search_weather_api_by_location(searched_location.capitalize())
		else:
			ip = geocoder.ip("me")
			weather_status = search_weather_api_by_location(ip.city.capitalize())

		context = {
			'weather_status' : self.add_days(weather_status),
			'today' : MainPage.get_todays_date(),

			'subscriptions' : Subscription.objects.all()
		}

		return render(request, self.template_name, context)


	def add_days(self, weather_status : dict) -> dict:

		""" Adds names to next days """

		tomorow_days_list = [calendar.day_name[(datetime.date.today() + datetime.timedelta(days = x)).weekday()] for x in range(1, 4)]

		for i in range(len(tomorow_days_list)):
			weather_status.days[i]['day_name'] = tomorow_days_list[i]

		return weather_status


	@staticmethod
	def get_todays_date() -> DateTimeResponse:

		""" Gets todays date number, month and days name """

		todays_date = datetime.datetime.now()

		curr_date = datetime.date.today()

		day_name = calendar.day_name[curr_date.weekday()]
		month_name = todays_date.strftime("%B")
		day = datetime.datetime.today().isoweekday()

		return DateTimeResponse(
				day_name = day_name,
				month_name = month_name,
				day = day
			)