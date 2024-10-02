from rest_framework import viewsets, generics
from .models import Cat
from .permissions import IsOwnerOrReadOnly
from .serializers import CatSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['get'], detail=False)
    def breed(self, request, pk=None):
        """ Получение списка пород, get запрос -> http://127.0.0.1:8000/api/v1/cat/breed """
        breeds = Cat.objects.values('breed')
        return Response({'breeds': [c['breed'] for c in breeds]})

    @action(methods=['get'], detail=False)
    def by_breed(self, request):
        """ Получение списка котят определенной породы по фильтру,
    get запрос -> http://127.0.0.1:8000/api/v1/cat/by_breed/?breed_name=вислоухий"""
        breed = request.query_params.get('breed_name')
        if not breed:
            breeds = Cat.objects.values('breed')
            return Response({"error": f"breed_name параметр обязателен, выбери породу: "
                                      f"{[c['breed'] for c in breeds]}"}, status=400)

        cats = self.queryset.filter(breed=breed)
        if not cats.exists():
            return Response({'error': f"Нет котят породы {breed}"})

        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data)


# class CatAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer
#     permission_classes = (IsOwnerOrReadOnly, )
#
#
# class CatAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer
#     permission_classes = (IsOwnerOrReadOnly, )
