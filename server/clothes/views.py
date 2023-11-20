import os, sys
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Clothes
from .serializers import ClothesSerializer

p = os.path.abspath('.') + r'\openweather'
sys.path.insert(1, p)
from openweatherapi import open_weather_api


# Create your views here.
class ClothesView(APIView):
    def get(self, request):
        queryset = Clothes.objects.all()
        serializer = ClothesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClothesSerializer(data=request.data)
        if serializer.is_valid():
            queryset = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothesDetailView(APIView):
    def get(self, request, pk):
        queryset = Clothes.objects.get(pk=pk)
        serializer = ClothesSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        queryset = Clothes.objects.get(pk=pk)
        serializer = ClothesSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = Clothes.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'Cloth deleted'}, status=status.HTTP_202_ACCEPTED)


class ClothesRecommendationView(APIView):
    def get(self, request, gender):
        gender_str = ["female", "male", "unisex"]
        weather_data = open_weather_api()
        # print(weather_data)

        if weather_data["temperature"] >= 30:
            season = "summer"
        elif weather_data["temperature"] >= 20:
            season = "autumn"
        elif weather_data["temperature"] >= 10:
            season = "spring"
        else:
            season = "winter"

        queryset = Clothes.objects.exclude(gender=gender_str[1-int(gender)])
        cloth_top = queryset.filter(
            Q(category='top') &
            Q(season=season)
        )
        serializer = ClothesSerializer(cloth_top, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
