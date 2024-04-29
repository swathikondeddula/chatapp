from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/<str:room_slug>/', ChatConsumer.as_asgi()),
]
