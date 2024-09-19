from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_home, name='home'),
    path('get_weather/', views.get_weather, name='get_weather'),
    path('download_weather/', views.download_weather, name='download_weather'),
]
