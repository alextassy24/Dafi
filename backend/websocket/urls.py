from django.urls import path
from .views import TemperatureAPI, PressureAPI

urlpatterns = [
    path('temperature-data/', TemperatureAPI.as_view(), name='temperature-data'),
    path('pressure-data/', PressureAPI.as_view(), name='pressure-data'),
]
