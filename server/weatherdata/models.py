from django.db import models


# class Analysis(models.Model):
#     weather_des = models.CharField(max_length=20)  # 날씨
#     temp = models.FloatField()  # 현재 온도
#     feels_like = models.FloatField()  # 체감 온도
#     temp_min = models.FloatField()  # 최저 기온
#     temp_max = models.FloatField()  # 최고 기온
#     humidity = models.FloatField()  # 습도
#     # pressure = models.FloatField()  # 기압
#     # wind_deg = models.FloatField()  # 풍향
#     wind_speed = models.FloatField()  # 풍속


class Clothes(models.Model):
    category = models.IntegerField()  # 입는 부위별 옷 구분
    cloth_type = models.CharField(max_length=32)  # 옷 종류
    color = models.CharField(max_length=16)  # 옷 색
    temp = models.IntegerField()  # 기온
    sex = models.IntegerField()  # 성별

    class Meta:
        ordering = ['category']
