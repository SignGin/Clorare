from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Clothes
from .serializers import ClothesSerializer


# Create your views here.
class ClothesList(APIView):
    def get(self, request):
        clothes = Clothes.objects.all()
        serializer = ClothesSerializer(clothes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClothesDetail(APIView):
    def get(self, request, pk):
        cloth = Clothes.objects.get(pk=pk)
        serializer = ClothesSerializer(cloth)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClothesDelete(APIView):
    def get(self, request, pk):
        cloth = Clothes.objects.get(pk=pk)
        cloth.delete()
        return Response({'message': 'Cloth deleted'}, status=status.HTTP_202_ACCEPTED)


class ClothesAdd(APIView):
    def post(self, request):
        serializer = ClothesSerializer(data=request.data)
        if serializer.is_valid():
            cloth = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothesRecommendation(APIView):
    def post(self, request):
        pass
