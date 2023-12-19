from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Weather
from .serializers import WeatherSerializer
from .openweatherapi import open_weather_api

# Weather Model Schema
wms_id = openapi.Schema(type=openapi.TYPE_INTEGER,
                        description='weather data id')
wms_weather = openapi.Schema(type=openapi.TYPE_STRING,
                             description='weather when you request')
wms_temperature = openapi.Schema(type=openapi.FORMAT_FLOAT,
                                 description='temperature when you request')
wms_feels_like = openapi.Schema(type=openapi.FORMAT_FLOAT,
                                description='feels like temperature when you request')
wms_daily_high = openapi.Schema(type=openapi.FORMAT_FLOAT,
                                description='daily high temperature when you request')
wms_daily_low = openapi.Schema(type=openapi.FORMAT_FLOAT,
                               description='daily low temperature when you request')
wms_humidity = openapi.Schema(type=openapi.TYPE_INTEGER,
                              description='humidity when you request')
wms_wind_speed = openapi.Schema(type=openapi.FORMAT_FLOAT,
                                description='wind speed when you request')
wms_time = openapi.Schema(type=openapi.FORMAT_DATETIME,
                          description='time when you request')


class WeatherList(APIView):
    @swagger_auto_schema(
        operation_id='All weather data',
        operation_description='Request all saved weather data',
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': wms_id,
                    'weather': wms_weather,
                    'temperature': wms_temperature,
                    'feels_like': wms_feels_like,
                    'daily_high': wms_daily_high,
                    'daily_low': wms_daily_low,
                    'humidity': wms_humidity,
                    'wind_speed': wms_wind_speed,
                    'time': wms_time
                })
            )
        }
    )
    def get(self, request):
        weather = Weather.objects.all()
        serializer = WeatherSerializer(weather, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WeatherRequest(APIView):
    @swagger_auto_schema(
        operation_id='Request weather data',
        operation_description='Save weather data when you request',
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': wms_id,
                    'weather': wms_weather,
                    'temperature': wms_temperature,
                    'feels_like': wms_feels_like,
                    'daily_high': wms_daily_high,
                    'daily_low': wms_daily_low,
                    'humidity': wms_humidity,
                    'wind_speed': wms_wind_speed,
                    'time': wms_time
                })
            )
        }
    )
    def get(self, request):
        serializer = WeatherSerializer(data=open_weather_api())

        if serializer.is_valid():
            weather_data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
