from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Weather
from .serializers import WeatherSerializer
from .openweatherapi import open_weather_api
from . import swagger as sw


class WeatherList(APIView):
    @swagger_auto_schema(
        operation_id='All weather data',
        operation_description='Request all saved weather data',
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': sw.wms_id,
                    'weather': sw.wms_weather,
                    'temperature': sw.wms_temperature,
                    'feels_like': sw.wms_feels_like,
                    'daily_high': sw.wms_daily_high,
                    'daily_low': sw.wms_daily_low,
                    'humidity': sw.wms_humidity,
                    'wind_speed': sw.wms_wind_speed,
                    'time': sw.wms_time
                })
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_400
                })
            )
        }
    )
    def get(self, request):
        try:
            if request.user.is_authenticated:
                weather = Weather.objects.all()
                serializer = WeatherSerializer(weather, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})


class WeatherRequest(APIView):
    @swagger_auto_schema(
        operation_id='Request weather data',
        operation_description='Save weather data when you request',
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': sw.wms_id,
                    'weather': sw.wms_weather,
                    'temperature': sw.wms_temperature,
                    'feels_like': sw.wms_feels_like,
                    'daily_high': sw.wms_daily_high,
                    'daily_low': sw.wms_daily_low,
                    'humidity': sw.wms_humidity,
                    'wind_speed': sw.wms_wind_speed,
                    'time': sw.wms_time
                })
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_400
                })
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_500
                })
            )
        }
    )
    def get(self, request):
        try:
            if request.user.is_authenticated:
                if open_weather_api()[0]:
                    return Response(open_weather_api()[1], status.HTTP_200_OK)
                serializer = WeatherSerializer(data=open_weather_api()[1])
                if serializer.is_valid():
                    weather_data = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})
