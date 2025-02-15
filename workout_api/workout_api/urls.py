"""
URL configuration for workout_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema =  get_schema_view(openapi.Info(title='Workout API',default_version='v1',
                                       description='API documentatation for the Personalized Workout Plan System'),
                                       public=True, permission_classes=[permissions.AllowAny],)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("workouts.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/',schema.with_ui('swagger',cache_timeout=0),name='shema-swagger-ui'),
    
]
