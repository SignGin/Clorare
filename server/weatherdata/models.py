from django.db import models


class Clothes(models.Model):
    category = models.IntegerField()  # 입는 부위별 옷 구분
    cloth_type = models.CharField(max_length=32)  # 옷 종류
    color = models.CharField(max_length=16)  # 옷 색
    temp = models.IntegerField()  # 기온
    sex = models.IntegerField()  # 성별
    image = models.ImageField(upload_to='clothes')

    class Meta:
        ordering = ['?']

    def __str__(self):
        return self.cloth_type
