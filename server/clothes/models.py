from django.db import models


class Clothes(models.Model):
    CATEGORY = [
        ('top', '상의'),
        ('bottom', '하의'),
        ('coat', '외투')
    ]
    GENDER = [
        ('0', '여자'),
        ('1', '남자'),
        ('2', '공용')
    ]
    category = models.CharField(max_length=10, choices=CATEGORY)  # ex) 상의, 하의
    cloth_type = models.CharField(max_length=10)  # ex) 티셔츠, 니트
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER)  # 여성, 남성, 무관
    image = models.ImageField(upload_to='clothes', null=True, blank=True)

    def __str__(self):
        return self.cloth_type

    class Meta:
        ordering = ['category']
