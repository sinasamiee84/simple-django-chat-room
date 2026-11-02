from django.urls import re_path
from .consumer import ChatConsumer

websocketurlpatterns = [

    re_path(r'ws/(?P<room_name>[^/]+)/$', ChatConsumer.as_asgi(), name='chat_room'),
]
