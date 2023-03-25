from django.contrib.auth.models import User
from rest_framework import serializers
from weatherdata.models import Clothes


# class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Analysis
#         fields = ['weather_des', 'temp', 'feels_like', 'temp_min', 'temp_max', 'humidity', 'wind_speed']


class ClothesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clothes
        fields = ['position', 'cloth', 'color']
