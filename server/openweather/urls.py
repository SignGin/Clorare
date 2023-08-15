from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    # 날씨 기록 조회
    path('', views.WeatherList.as_view(), name='weather'),
    # 날씨 기록 요청
    path('request/', views.WeatherRequest.as_view(), name='weather-request'),
]
