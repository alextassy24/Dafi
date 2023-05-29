from django.urls import path
from .consumers import BaseConsumer, SendConsumer

websocket_urlpatterns = [
    path('ws/base/', BaseConsumer.as_asgi()),
    path('ws/send/', SendConsumer.as_asgi())
]
