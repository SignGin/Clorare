from django.contrib.auth.models import User
from requests import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from restapi.serializers import ClothesSerializer
from weatherdata.models import Clothes
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from weatherdata.api import get_weather


# class AnalysisViewSet(viewsets.ModelViewSet):
#     queryset = Analysis.objects.all()
#     serializer_class = AnalysisSerializer


class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer


class Recommendation(viewsets.ModelViewSet):
    w_data = dict()
    get_weather(w_data)
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

    def classification(self, request):
        queryset = self.get_queryset()
        serializer = ClothesSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        return user.accounts.all()