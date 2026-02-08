from rest_framework import status
from rest_framework import response
from django.conf import settings
import requests
def get_weather_data(city_name):
    if not city_name :
        return {'message':'City not found.'}
    
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q':city_name,
        'appid':settings.WEATHER_API_KEY,
        'units':'metric'
    }
    
    try:
        responses = requests.get(url, params=params)
        if responses.status_code != 200:
            return {'error':'City not found or weather service error'}
        
        data = responses.json()
        weather_data = {
            'city':data['name'],
            'temperature':data['main']['temp'],
            'description':data['weather'][0]['description'],
            'humidity':data['main']['humidity'],
            'pressure':data['main']['pressure'],
            'wind speed':data['wind']['speed'],
            'country':data['sys']['country'],
        }
        return weather_data

    except requests.exceptions.RequestException:
        return {'message':'Weather service is unavailable.'}
    

