from rest_framework import serializers
from .models import Clothes


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'


class ClorareSerializer(serializers.Serializer):
    top = serializers.JSONField()
    bot = serializers.JSONField()
    coat = serializers.JSONField(allow_null=True)
    gender = serializers.CharField(max_length=6)
    w_data = serializers.JSONField()
