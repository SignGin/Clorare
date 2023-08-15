from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Weather
from .serializers import WeatherSerializer
from .openweatherapi import open_weather_api


class WeatherList(APIView):
    def get(self, request):
        weather = Weather.objects.all()
        serializer = WeatherSerializer(weather, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WeatherRequest(APIView):
    def get(self, request):
        serializer = WeatherSerializer(data=open_weather_api())

        if serializer.is_valid():
            weather_data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
