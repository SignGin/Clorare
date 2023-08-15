from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Weather
from .serializers import WeatherSerializer
from .openweatherapi import open_weather_api


class WeatherRequest(APIView):
    def get(self, request):
        serializer = WeatherSerializer(data=open_weather_api())

        if serializer.is_valid():
            weather_data = serializer.save()
            print("시리얼라이저", serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
