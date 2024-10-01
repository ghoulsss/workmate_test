from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from cats.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/catlist', CatAPIList.as_view()),
    path('api/catlist/<int:pk>', APIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
