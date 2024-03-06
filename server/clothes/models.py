from django.db import models


class Clothes(models.Model):
    CATEGORY = [
        ('top', '상의'),
        ('bottom', '하의'),
        ('coat', '외투')
    ]
    GENDER = [
        ('female', '여자'),
        ('male', '남자'),
        ('unisex', '공용')
    ]
    SEASON = [
        ('spring', '봄'),
        ('summer', '여름'),
        ('autumn', '가을'),
        ('winter', '겨울')
    ]
    category = models.CharField(max_length=6, choices=CATEGORY)  # ex) 상의, 하의
    cloth_type = models.CharField(max_length=20)  # ex) 티셔츠, 니트
    season = models.CharField(max_length=6, choices=SEASON)  # ex) 봄, 여름, 가을, 겨울
    gender = models.CharField(max_length=6, choices=GENDER)  # 여성, 남성, 무관
    image = models.ImageField(default="default_image.jpg", null=True, blank=True)

    def __str__(self):
        return self.cloth_type

    class Meta:
        ordering = ['category']
