import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from weatherdata.api import get_weather
from weatherdata.models import Clothes
from .serializers import ClothesSerializer
from django.http import HttpResponse


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def request_api(request):
    if request.method == 'GET':
        query_set = Clothes.objects.all()
        serializer = ClothesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClothesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def request_cloth(request, pk):
    try:
        obj = Clothes.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"MESSAGE": "Error, Please Check DB"}, status=401)

    if request.method == 'GET':
        serializer = ClothesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClothesSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def request_reco(request, sex):
    if request.method == 'GET' and (sex == 0 or sex == 1):
        try:
            w_data = get_weather()
            if w_data["main"]["feels_like"] < 16:
                temp = 0  # 추움
            elif w_data["main"]["feels_like"] < 22:
                temp = 1  # 조금 추움
            elif w_data["main"]["feels_like"] < 27:
                temp = 2  # 적당함
            elif w_data["main"]["feels_like"] >= 27:
                temp = 3  # 더움
        except:
            return JsonResponse({"MESSAGE": "Error, Please Check Api Setting"}, status=401)

        w_temp_diff = round(w_data["main"]["temp_max"] - w_data["main"]["temp_min"], 2)

        obj_0 = Clothes.objects.filter(Q(sex=sex) | Q(sex=2)).filter(Q(category=0) & Q(temp=temp)).values()[0]
        obj_1 = Clothes.objects.filter(Q(sex=sex) | Q(sex=2)).filter(Q(category=1) & Q(temp=temp)).values()[0]
        obj_2 = Clothes.objects.filter(Q(category=2) & Q(temp=temp if (w_temp_diff >= 10 or temp < 2) else 3)).values()[0]

        context = {
            'top': {
                'cloth_type': obj_0['cloth_type'],
                'color': obj_0['color'],
                'image': "/media" + obj_0['image'],
            },
            'bot': {
                'cloth_type': obj_1['cloth_type'],
                'color': obj_1['color'],
                'image': "/media" + obj_1['image'],
            },
            'overcoat': {
                'cloth_type': obj_2['cloth_type'],
                'color': obj_2['color'],
                'image': "/media" + obj_2['image'],
            },
            'sex': sex,
            'w_data': w_data["weather"][0]["main"],
            'w_temp': w_data["main"]["temp"],
            'w_temp_diff': w_temp_diff,
        }

        print(json.dumps(context))
        return JsonResponse(context, safe='False')

    elif sex != 0 and sex != 1:
        return JsonResponse({"MESSAGE": "Error, Unknown Gender Value"}, status=401)

    else:
        return JsonResponse({"MESSAGE": "Error, Please try again"}, status=404)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def request_weather(request):
    if request.method == 'GET':
        try:
            w_data = get_weather()
        except:
            return JsonResponse({"MESSAGE": "Error, Please Check Api Setting"}, status=401)

        context = {
            'w_data': w_data["weather"][0]["main"],
            'w_temp': w_data["main"]["temp"],
            'w_feels_like': w_data["main"]["feels_like"],
            'w_daily_range': w_data["main"]["temp_max"] - w_data["main"]["temp_min"],
            'w_humidity': w_data["main"]["humidity"],
            'w_wind_speed': w_data["wind"]["speed"],
        }

        print(json.dumps(context))
        return JsonResponse(context, safe='False')
