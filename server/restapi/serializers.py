from rest_framework import serializers
from weatherdata.models import Clothes


class ClothesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clothes
        fields = ['category', 'cloth_type', 'color', 'temp', 'sex', 'pk']
