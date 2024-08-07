from django.shortcuts import render
import requests
from datetime import datetime

def index(request):
    weather_data = {}
    if 'city' in request.GET:
        city = request.GET.get('city')
        api_key = 'a88d824f849bb62d68baea50c901db75'
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        response = requests.get(api_url)
        data = response.json()
        
        if data['cod'] == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'datetime': datetime.fromtimestamp(data['dt']),
                'error': None
            }
        else:
            weather_data['error'] = 'City not found!'
    return render(request, 'weather/index.html', {'weather_data': weather_data})
