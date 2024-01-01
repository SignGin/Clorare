from rest_framework import serializers
from .models import Clothes


def dec_b64_img(dict_data):
    import base64
    from django.conf import settings

    if dict_data['image']:
        header, data = dict_data['image'].split(';base64,')
        data_format, ext = header.split('/')

        image_name = dict_data['cloth_type']
        dec_data = base64.b64decode(data)
        image_root = f'{settings.MEDIA_ROOT}\\clothes\\{image_name}.{ext}'

        with open(image_root, 'wb') as f:
            f.write(dec_data)

        return f'/{image_name}.{ext}'
    return None


class ClothesSerializer(serializers.ModelSerializer):
    image = serializers.CharField()

    class Meta:
        model = Clothes
        fields = '__all__'


class ClorareSerializer(serializers.Serializer):
    top = serializers.JSONField()
    bot = serializers.JSONField()
    coat = serializers.JSONField(allow_null=True)
    gender = serializers.CharField(max_length=6)
    w_data = serializers.JSONField()
