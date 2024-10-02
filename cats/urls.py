from django.urls import path
from .views import *

urlpatterns = [
    path('catlist/', CatAPIView.as_view()),  # Получение списка всех котят(get запрос -> http://127.0.0.1:8000/api/v1/cat)

    path('catdetail/<int:pk>/', CatAPIUpdate.as_view()),  # получение информации о котенке(get и put запросом -> http://127.0.0.1:8000/api/v1/cat/3/)
    path('catdetail/<int:pk>/', CatAPIUpdate.as_view()),  # не работает добавление

    path('catdelete/<int:pk>/', CatAPIDestroy.as_view()),  # Удаление информации о котенке(delete -> http://127.0.0.1:8000/api/v1/catdelete/
    path('breed/', BreedListView.as_view(), name='breed-list'),  # Получение списка пород (get запрос -> http://127.0.0.1:8000/api/v1/breed)
    path('by_breed/', CatByBreedView.as_view(), name='cat-by-breed'),  # Получение списка котят определенной породы по фильтру.(get запрос -> http://127.0.0.1:8000/api/v1/by_breed/?breed_name=британец)
]
