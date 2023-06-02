from django.urls import path
from .consumers import SendConsumer

websocket_urlpatterns = [
    path('ws/send/', SendConsumer.as_asgi()),
]
