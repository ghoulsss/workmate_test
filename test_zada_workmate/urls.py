from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cats.views import *


router = routers.SimpleRouter()
router.register(r'cat', CatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/cat/

    # path('api/catlist', ), # список всех кошек
    # path('api/catlist/<int:pk>/', CatViewSet.as_view()), # менять запись

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
