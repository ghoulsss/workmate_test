from rest_framework import viewsets, generics
from .models import Cat
from .serializers import CatSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


# class CatAPIOne(generics.RetrieveAPIView): # Получение подробной информации о котенке.
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatAPIBreed(generics.RetrieveAPIView): # Получение списка пород
#     queryset = Cat # переписать orm запрос для пород только
#     serializer_class = CatSerializer