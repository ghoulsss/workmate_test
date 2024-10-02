from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Cat
from .serializers import CatSerializer
from rest_framework.response import Response


class BreedListView(APIView):
    """ Получение списка пород котят """
    def get(self, request):
        breeds = Cat.objects.values('breed').distinct()
        return Response({'breeds': [c['breed'] for c in breeds]})


class CatByBreedView(APIView):
    """ Получение списка котят определенной породы по фильтру """
    def get(self, request):
        breed = request.query_params.get('breed_name')
        if not breed:
            breeds = Cat.objects.values('breed').distinct()
            return Response({
                "error": f"breed_name параметр обязателен, выбери породу: "
                          f"{[c['breed'] for c in breeds]}"})

        cats = Cat.objects.filter(breed=breed)
        if not cats.exists():
            return Response({'error': f"Нет котят породы {breed}"})

        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)


class CatAPIUpdate(generics.RetrieveUpdateAPIView):  # Изменение и получение информации о котенке(get и put запросом -> http://127.0.0.1:8000/api/v1/cat/3/)
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    #permission_classes = (IsOwnerOrReadOnly, )


class CatAPIDestroy(generics.DestroyAPIView):  # Удаление информации о котенке(delete -> http://127.0.0.1:8000/api/v1/catdelete/3/)
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    #permission_classes = (IsOwnerOrReadOnly, )


class CatAPIView(generics.ListAPIView):  # Получение списка всех котят(get запрос -> http://127.0.0.1:8000/api/v1/catlist/)
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
