from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Clothes
from .serializers import ClothesSerializer


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
