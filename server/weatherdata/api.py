import requests
import json
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

ROOT_DIR = os.path.dirname(Path(__file__).resolve().parent)
SECRETS_PATH = os.path.join(ROOT_DIR, 'secrets.json')
secrets = json.loads(open(SECRETS_PATH).read())


def get_secret(setting):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


API_KEY = get_secret("API_KEY")

city = "Seoul"
lang = "kr"


def get_weather():
    try:
        api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang={lang}&units=metric"

        result = requests.get(api)
        w_data = json.loads(result.text)

        # print(w_data["name"],"의 날씨입니다.")
        # print("날씨는 ",w_data["weather"][0]["description"],"입니다.")
        # print("현재 온도는 ",w_data["main"]["temp"],"입니다.")
        # print("하지만 체감 ",w_data["main"]["feels_like"],"일 거에요.")
        # print("최저 기온은 ",w_data["main"]["temp_min"],"입니다.")
        # print("최고 기온은 ",w_data["main"]["temp_max"],"입니다.")
        # print("습도는 ",w_data["main"]["humidity"],"입니다.")
        # print("기압은 ",w_data["main"]["pressure"],"입니다.")
        # print("풍향은 ", w_data["wind"]["deg"],"입니다.")
        # print("풍속은 ", w_data["wind"]["speed"],"입니다.")

        return w_data

    except:
        return 999
