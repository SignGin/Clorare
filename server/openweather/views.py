import os, requests, json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Weather
from .serializers import WeatherSerializer

API_KEY = os.environ.get("OPENWEATHER_API_KEY")
city = "Seoul"
language = "kr"


class WeatherRequest(APIView):
    def get(self, request):
        api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang={language}&units=metric"
        result = requests.get(api)
        weather = json.loads(result.text)

        weather_data = {
            "temperature": weather["main"]["temp"],
            "feels_like": weather["main"]["feels_like"],
            "daily_high": weather["main"]["temp_max"],
            "daily_low": weather["main"]["temp_min"],
            "humidity": weather["main"]["humidity"],
            "wind_speed": weather["wind"]["speed"]
        }
        serializer = WeatherSerializer(data=weather_data)

        if serializer.is_valid():
            weather_data = serializer.save()
            print("시리얼라이저", serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

