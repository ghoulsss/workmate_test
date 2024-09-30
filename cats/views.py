from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from .models import Breed, Cat
from .serializers import BreedSerializer, KittenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated]  # Защита для создания/изменения/удаления котят

    @action(detail=False, methods=['get'])
    def by_breed(self, request, breed_id=None):
        kittens = self.queryset.filter(breed_id=breed_id)
        serializer = self.get_serializer(kittens, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Сохраняем ID текущего пользователя как владельца

    def perform_update(self, serializer):
        if serializer.instance.owner != self.request.user:
            raise PermissionDenied("Не вы добавили кота")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("Не вы добавили кота")
        instance.delete()

