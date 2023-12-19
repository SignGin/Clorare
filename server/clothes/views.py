import os, sys
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Clothes
from .serializers import ClothesSerializer, ClorareSerializer

p = os.path.abspath('.') + r'\openweather'
sys.path.insert(1, p)
from openweatherapi import open_weather_api

# Request Parameter
rp_id = openapi.Parameter('id', openapi.IN_PATH, type=openapi.TYPE_INTEGER,
                          description='cloth id')
rp_gender = openapi.Parameter('id', openapi.IN_PATH, type=openapi.TYPE_INTEGER, enum=[0, 1, 2],
                              description='gender to wear cloth\nfemale=0\nmale=1\nunisex=2')

# Cloth Model Schema
cms_id = openapi.Schema(type=openapi.TYPE_INTEGER,
                        description='cloth id')
cms_category = openapi.Schema(type=openapi.TYPE_STRING, enum=['top', 'bottom', 'coat'],
                              description='cloth category\nmax_length:6')
cms_cloth_type = openapi.Schema(type=openapi.TYPE_STRING,
                                description='cloth name\nex) t-shirts, sweater, jeans')
cms_season = openapi.Schema(type=openapi.TYPE_STRING, enum=['spring', 'summer', 'autumn', 'winter'],
                            description='season to wear')
cms_gender = openapi.Schema(type=openapi.TYPE_STRING, enum=['female', 'male', 'unisex'],
                            description='gender to wear cloth')
cms_image = openapi.Schema(type=openapi.TYPE_FILE,
                           description='cloth image')

# Weather Model Schema
wms_weather = openapi.Schema(type=openapi.TYPE_STRING,
                             description='weather when you request')
wms_temperature = openapi.Schema(type=openapi.TYPE_NUMBER,
                                 description='temperature when you request')
wms_feels_like = openapi.Schema(type=openapi.TYPE_NUMBER,
                                description='feels like temperature when you request')
wms_daily_high = openapi.Schema(type=openapi.TYPE_NUMBER,
                                description='daily high temperature when you request')
wms_daily_low = openapi.Schema(type=openapi.TYPE_NUMBER,
                               description='daily low temperature when you request')
wms_humidity = openapi.Schema(type=openapi.TYPE_INTEGER,
                              description='humidity when you request')
wms_wind_speed = openapi.Schema(type=openapi.TYPE_NUMBER,
                                description='wind speed when you request')

# System Message Schema
sms_202 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='202 accepted message')
sms_400 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='400 error message')
sms_500 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='500 error message')

# Create your views here.
class ClothesView(APIView):
    @swagger_auto_schema(
        operation_id='All clothes data',
        operation_description='Request all clothes data',
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': cms_id,
                    'category': cms_category,
                    'cloth_type': cms_cloth_type,
                    'season': cms_season,
                    'gender': cms_gender,
                    'image': cms_image
                })
            )
        }
    )
    def get(self, request):
        queryset = Clothes.objects.all()
        serializer = ClothesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_id='Add cloth data',
        operation_description='Add user custom cloth data',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'category': cms_category,
                'cloth_type': cms_cloth_type,
                'season': cms_season,
                'gender': cms_gender,
                'image': cms_image
            },
            required=['category', 'cloth_type', 'season', 'gender']
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': cms_id,
                    'category': cms_category,
                    'cloth_type': cms_cloth_type,
                    'season': cms_season,
                    'gender': cms_gender,
                    'image': cms_image
                })
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                'Fail', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sms_400
                })
            )
        }
    )
    def post(self, request):
        serializer = ClothesSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothesDetailView(APIView):
    @swagger_auto_schema(
        operation_id='Detail cloth data',
        operation_description='Request cloth data by selecting cloth id number',
        manual_parameters=[rp_id],
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': cms_id,
                    'category': cms_category,
                    'cloth_type': cms_cloth_type,
                    'season': cms_season,
                    'gender': cms_gender,
                    'image': cms_image
                })
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sms_500
                })
            )
        }
    )
    def get(self, request, pk):
        queryset = Clothes.objects.get(pk=pk)
        serializer = ClothesSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_id='Update cloth data',
        operation_description='Update user custom cloth data',
        manual_parameters=[rp_id],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'category': cms_category,
                'cloth_type': cms_cloth_type,
                'season': cms_season,
                'gender': cms_gender,
                'image': cms_image
            },
            required=[]
        ),
        responses={
            status.HTTP_202_ACCEPTED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': cms_id,
                    'category': cms_category,
                    'cloth_type': cms_cloth_type,
                    'season': cms_season,
                    'gender': cms_gender,
                    'image': cms_image
                })
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                'Fail', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sms_400
                })
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sms_500
                })
            )
        }
    )
    def put(self, request, pk):
        queryset = Clothes.objects.get(pk=pk)
        serializer = ClothesSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id='Delete cloth data',
        operation_description='Delete cloth data by selecting cloth id number',
        manual_parameters=[rp_id],
        responses={
            status.HTTP_202_ACCEPTED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sms_202
                })
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sms_500
                })
            )
        }
    )
    def delete(self, request, pk):
        queryset = Clothes.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'Cloth deleted'}, status=status.HTTP_202_ACCEPTED)


class ClothesRecommendationView(APIView):
    @swagger_auto_schema(
        operation_id='Cloth recommendation',
        operation_description='Recommend clothes at random',
        manual_parameters=[rp_gender],
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'top': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'category': cms_category,
                        'cloth_type': cms_cloth_type,
                        'season': cms_season,
                        'gender': cms_gender,
                        'image': cms_image
                    }),
                    'bot': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'category': cms_category,
                        'cloth_type': cms_cloth_type,
                        'season': cms_season,
                        'gender': cms_gender,
                        'image': cms_image
                    }),
                    'coat': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'category': cms_category,
                        'cloth_type': cms_cloth_type,
                        'season': cms_season,
                        'gender': cms_gender,
                        'image': cms_image
                    }),
                    'gender': cms_gender,
                    'w_data': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'weather': wms_weather,
                        'temperature': wms_temperature,
                        'feels_like': wms_feels_like,
                        'daily_high': wms_daily_high,
                        'daily_low': wms_daily_low,
                        'humidity': wms_humidity,
                        'wind_speed': wms_wind_speed
                    })
                })
            )
        }
    )
    def get(self, request, gender):
        gender_str = ["female", "male", "unisex"]
        weather_data = open_weather_api()

        if weather_data["temperature"] >= 30:
            season = "summer"
        elif weather_data["temperature"] >= 20:
            season = "autumn"
        elif weather_data["temperature"] >= 10:
            season = "spring"
        else:
            season = "winter"

        queryset = Clothes.objects.exclude(gender=gender_str[1-int(gender)])
        queryset = queryset.filter(season=season)

        cloth_top = queryset.filter(category="top").order_by("?").first()
        cloth_bottom = queryset.filter(category="bottom").order_by("?").first()
        cloth_coat = queryset.filter(category="coat").order_by("?").first()

        serialized_top = ClothesSerializer(cloth_top).data
        serialized_bottom = ClothesSerializer(cloth_bottom).data
        serialized_coat = ClothesSerializer(cloth_coat).data

        context = {
            "top": serialized_top,
            "bot": serialized_bottom,
            "coat": serialized_coat,
            "gender": gender_str[gender],
            "w_data": weather_data
        }

        serializer = ClorareSerializer(context)
        return Response(serializer.data, status=status.HTTP_200_OK)
