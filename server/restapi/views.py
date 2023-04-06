import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from weatherdata.api import get_weather
from weatherdata.models import Clothes
from .serializers import ClothesSerializer
from django.http import HttpResponse


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


@csrf_exempt
def request_cloth(request, pk):
    obj = Clothes.objects.get(pk=pk)

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


@csrf_exempt
def request_reco(request, sex):
    obj = Clothes.objects.all()

    if request.method == 'GET':
        w_data = get_weather()
        if w_data["main"]["feels_like"] < 16:
            temp = 0
        elif w_data["main"]["feels_like"] < 22:
            temp = 1
        elif w_data["main"]["feels_like"] < 27:
            temp = 2
        elif w_data["main"]["feels_like"] >= 27:
            temp = 3
        else:
            pass

        obj_0 = Clothes.objects.filter(Q(sex=sex) | Q(sex=2)).filter(Q(category=0) & Q(temp=temp)).values()[0]
        obj_1 = Clothes.objects.filter(Q(sex=sex) | Q(sex=2)).filter(Q(category=0) & Q(temp=temp)).values()[0]

        context = {
            'top': obj_0,
            'bot': obj_1,
            'w_data': w_data["weather"][0]["main"],
            'w_temp': w_data["main"]["temp"],
            'w_feels_like': w_data["main"]["feels_like"],
            'w_daily_range': w_data["main"]["temp_max"]-w_data["main"]["temp_min"],
            'w_humidity': w_data["main"]["humidity"],
            'w_wind_speed': w_data["wind"]["speed"],
        }

        print(json.dumps(context))
        return JsonResponse(context, safe='False')
        # serializer = ClothesSerializer(obj, many=True)
        # return JsonResponse(serializer.data, safe=False)

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




