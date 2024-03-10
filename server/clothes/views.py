from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Clothes
from .serializers import ClothesSerializer, ClorareSerializer
from . import swagger as sw
from .utils import dec_b64_img, modifying_image_path
from openweather.openweatherapi import open_weather_api


# Create your views here.
class ClothesView(APIView):
    @swagger_auto_schema(
        operation_id='All clothes data',
        operation_description='Request all clothes data',
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': sw.cms_id,
                    'category': sw.cms_category,
                    'cloth_type': sw.cms_cloth_type,
                    'season': sw.cms_season,
                    'gender': sw.cms_gender,
                    'image': sw.cms_image
                })
            )
        }
    )
    def get(self, request):
        try:
            if request.user.is_authenticated:
                queryset = Clothes.objects.all()
                serializer = ClothesSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})

    @swagger_auto_schema(
        operation_id='Add cloth data',
        operation_description='Add user custom cloth data',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'category': sw.cms_category,
                'cloth_type': sw.cms_cloth_type,
                'season': sw.cms_season,
                'gender': sw.cms_gender,
                'image': sw.cms_image
            },
            required=['category', 'cloth_type', 'season', 'gender']
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': sw.cms_id,
                    'category': sw.cms_category,
                    'cloth_type': sw.cms_cloth_type,
                    'season': sw.cms_season,
                    'gender': sw.cms_gender,
                    'image': sw.cms_image
                })
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_400
                })
            )
        }
    )
    def post(self, request):
        try:
            if request.user.is_authenticated:
                context = {
                    'category': request.data['category'],
                    'cloth_type': request.data['cloth_type'],
                    'season': request.data['season'],
                    'gender': request.data['gender'],
                    'image': dec_b64_img(request.data)
                }
                serializer = ClothesSerializer(data=context)
                if serializer.is_valid():
                    queryset = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})


class ClothesDetailView(APIView):
    @swagger_auto_schema(
        operation_id='Detail cloth data',
        operation_description='Request cloth data by selecting cloth id number',
        manual_parameters=[sw.rp_id],
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': sw.cms_id,
                    'category': sw.cms_category,
                    'cloth_type': sw.cms_cloth_type,
                    'season': sw.cms_season,
                    'gender': sw.cms_gender,
                    'image': sw.cms_image
                })
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_500
                })
            )
        }
    )
    def get(self, request, pk):
        try:
            if request.user.is_authenticated:
                queryset = Clothes.objects.get(pk=pk)
                serializer = ClothesSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})

    @swagger_auto_schema(
        operation_id='Update cloth data',
        operation_description='Update user custom cloth data',
        manual_parameters=[sw.rp_id],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'category': sw.cms_category,
                'cloth_type': sw.cms_cloth_type,
                'season': sw.cms_season,
                'gender': sw.cms_gender,
                'image': sw.cms_image
            },
            required=[]
        ),
        responses={
            status.HTTP_202_ACCEPTED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': sw.cms_id,
                    'category': sw.cms_category,
                    'cloth_type': sw.cms_cloth_type,
                    'season': sw.cms_season,
                    'gender': sw.cms_gender,
                    'image': sw.cms_image
                })
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_400
                })
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_500
                })
            )
        }
    )
    def put(self, request, pk):
        try:
            if request.user.is_authenticated:
                queryset = Clothes.objects.get(pk=pk)
                serializer = ClothesSerializer(queryset, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})

    @swagger_auto_schema(
        operation_id='Delete cloth data',
        operation_description='Delete cloth data by selecting cloth id number',
        manual_parameters=[sw.rp_id],
        responses={
            status.HTTP_202_ACCEPTED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_202
                })
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_500
                })
            )
        }
    )
    def delete(self, request, pk):
        try:
            if request.user.is_authenticated:
                queryset = Clothes.objects.get(pk=pk)
                queryset.delete()
                return Response({'message': 'Cloth deleted'}, status=status.HTTP_202_ACCEPTED)
            return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})


class ClothesRecommendationView(APIView):
    @swagger_auto_schema(
        operation_id='Cloth recommendation',
        operation_description='Recommend clothes at random',
        manual_parameters=[sw.rp_gender],
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'top': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'category': sw.cms_category,
                        'cloth_type': sw.cms_cloth_type,
                        'season': sw.cms_season,
                        'gender': sw.cms_gender,
                        'image': sw.cms_image
                    }),
                    'bot': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'category': sw.cms_category,
                        'cloth_type': sw.cms_cloth_type,
                        'season': sw.cms_season,
                        'gender': sw.cms_gender,
                        'image': sw.cms_image
                    }),
                    'coat': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'category': sw.cms_category,
                        'cloth_type': sw.cms_cloth_type,
                        'season': sw.cms_season,
                        'gender': sw.cms_gender,
                        'image': sw.cms_image
                    }),
                    'gender': sw.cms_gender,
                    'w_data': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'weather': sw.wms_weather,
                        'temperature': sw.wms_temperature,
                        'feels_like': sw.wms_feels_like,
                        'daily_high': sw.wms_daily_high,
                        'daily_low': sw.wms_daily_low,
                        'humidity': sw.wms_humidity,
                        'wind_speed': sw.wms_wind_speed
                    })
                })
            )
        }
    )
    def get(self, request, gender):
        try:
            if request.user.is_authenticated:
                gender_str = ["female", "male"]
                weather_data = open_weather_api()[1]

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
                    "top": modifying_image_path(serialized_top),
                    "bot": modifying_image_path(serialized_bottom),
                    "coat": modifying_image_path(serialized_coat),
                    "gender": gender_str[gender],
                    "w_data": weather_data
                }

                serializer = ClorareSerializer(context)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})


class ClothesCleanUpView(APIView):
    @swagger_auto_schema(
        operation_id='Delete all clothes data',
        operation_description='Delete all clothes data',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'key': sw.del_key
            },
            required=['key']
        ),
        responses={
            status.HTTP_202_ACCEPTED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_202
                })
            ),
            status.HTTP_403_FORBIDDEN: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_403
                })
            )
        }
    )
    def post(self, request):
        try:
            if request.user.is_authenticated:
                if request.data['key'] == "delete all clothes data":
                    queryset = Clothes.objects.all()
                    queryset.delete()
                    return Response({'message': 'Cloth deleted'}, status=status.HTTP_202_ACCEPTED)
                return Response({'message': 'Incorrect delete key'}, status=status.HTTP_403_FORBIDDEN)
            return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)})

