from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url ='http://api.openweathermap.org/data/2.5/weather?q={}&appid=2d699f11b36ddcd5306c2c3fc893b671'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_date = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city':city.name ,
            'temperature': round((int(r['main']['temp'])-32)*0.55),
            'description': r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }

        weather_date.append(city_weather)

    context = {'weather_date':weather_date,'form':form}
    return render(request,'weathe/index.html',context)
