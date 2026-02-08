from django.shortcuts import render
from .serializers import WeatherSerializer
from .models import Weather
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from .weather_service import get_weather_data


@cache_page(60*5)  # Cache for 5 mins
@api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
def get_weather(request):
    if not request.user.is_authenticated:
        return Response({'error':'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
    
    city = request.query_params.get('city')
    if not city:
        return Response({'error':'City is required'}, status=status.HTTP_400_BAD_REQUEST)

    data = get_weather_data(city)
    if 'error' in data:
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    
    wind_speed = data.get('wind speed')
    if not wind_speed:
        return Response({'error':'Wind speed mission from weather data'}, status=400)
    
    weather_record = Weather.objects.create(
        user=request.user,
        city=data['city'],
        temp=data['temperature'],
        description=data['description'],
        country=data.get('country'),
        humidity=data.get('humidity'),
        wind_speed=data.get('wind_speed'),
    )

    response_data = data.copy()
    response_data['timestamp'] = weather_record.timestamp
    return Response(response_data, status=status.HTTP_200_OK)



# Notes
"""
Caching API Responses = It keeps a copy of the answer for a little while. Next time someone asks, I just give them the copy, and not need to run my view again.


"""