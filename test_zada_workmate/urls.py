from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cats.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('cats.urls')),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
