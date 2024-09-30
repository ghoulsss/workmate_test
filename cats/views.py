from rest_framework import viewsets, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView

from .models import Cat
from .serializers import CatSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class CatAPIList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class WomenAPIView(APIView):
    def get(self, request):
        w = Cat.objects.all()
        return Response({'posts': CatSerializer(w, many=True).data})

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Cat.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CatSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        # здесь код для удаления записи с переданным pk

        return Response({"post": "delete post " + str(pk)})


# class CatViewSet(viewsets.ModelViewSet):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer
#     permission_classes = [IsAuthenticated]  # Защита для создания/изменения/удаления котят
#
#     @action(detail=False, methods=['get'])
#     def by_breed(self, request, breed_id=None):
#         kittens = self.queryset.filter(breed_id=breed_id)
#         serializer = self.get_serializer(kittens, many=True)
#         return Response(serializer.data)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)  # Сохраняем ID текущего пользователя как владельца
#
#     def perform_update(self, serializer):
#         if serializer.instance.owner != self.request.user:
#             raise PermissionDenied("Не вы добавили кота")
#         serializer.save()
#
#     def perform_destroy(self, instance):
#         if instance.owner != self.request.user:
#             raise PermissionDenied("Не вы добавили кота")
#         instance.delete()

