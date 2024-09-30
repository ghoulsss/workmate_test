from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from cats.views import CatViewSet, BreedViewSet

router = DefaultRouter()

router.register(r'kittens', CatViewSet, basename='kitten')
router.register(r'breeds', BreedViewSet, basename='breed')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
