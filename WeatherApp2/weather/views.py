from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import City
from .forms import CityForm
import datetime


def index(request):
	if 'city' in request.POST:
		city = request.POST['city']
	else:
		city = 'Minsk'

	appid = "7eb09fff6141b9669c7dba7d365d6fdf"
	URL = "https://api.openweathermap.org/data/2.5/weather"
	PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
	r = requests.get(url=URL, params=PARAMS)
	res = r.json()

	temp = res["main"]["temp"]
	icon = res['weather'][0]['icon']

	code = res["sys"]["country"]
	wind = res["wind"]["speed"]
	description = res['weather'][0]['description']

	day = datetime.date.today()

	# all_cities.append(city_info)

	# contex = {'all_info': all_cities, 'form': form}

	return render(request, 'weather/index.html', {'temp': temp, 'icon': icon, 'code': code, 'wind': wind,
	                                              'description': description, 'day': day, 'city': city})
