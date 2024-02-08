import os, requests, json

from openweather.models import Weather
from openweather.serializers import WeatherSerializer

API_KEY = os.environ.get("OPENWEATHER_API_KEY")
city = "Seoul"
language = "kr"


def date_comparison():
    queryset = Weather.objects.all().order_by("-time").first()
    serializer = WeatherSerializer(queryset)

    import datetime
    import pytz

    datetime_string = datetime.datetime.strptime(serializer.data['time'], '%Y-%m-%dT%H:%M:%S.%f%z')
    time_now = datetime.datetime.now(pytz.timezone('Asia/Seoul')) - datetime.timedelta(hours=1)

    return datetime_string > time_now, serializer.data


def open_weather_api():
    comparison = date_comparison()
    if comparison[0]:
        return comparison

    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang={language}&units=metric"
    result = requests.get(api)
    weather = json.loads(result.text)

    weather_data = {
        "weather": weather["weather"][0]["main"],
        "temperature": weather["main"]["temp"],
        "feels_like": weather["main"]["feels_like"],
        "daily_high": weather["main"]["temp_max"],
        "daily_low": weather["main"]["temp_min"],
        "humidity": weather["main"]["humidity"],
        "wind_speed": weather["wind"]["speed"]
    }
    return comparison[0], weather_data
