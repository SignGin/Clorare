from django.db import models


class Weather(models.Model):
    temperature = models.FloatField()
    feels_like = models.FloatField()
    daily_high = models.FloatField()
    daily_low = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.time
