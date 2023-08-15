import os, requests, json

API_KEY = os.environ.get("OPENWEATHER_API_KEY")
city = "Seoul"
language = "kr"


def open_weather_api():
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
    return weather_data
