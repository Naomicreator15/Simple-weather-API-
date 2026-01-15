from django.urls import path
from weather.views import WeatherDetailView

urlpatterns = [
    path('weather/', WeatherDetailView.as_view(), name='weather_detail'),

]