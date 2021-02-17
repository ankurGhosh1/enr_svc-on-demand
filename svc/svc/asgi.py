import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from svc import consumers
from django.urls import re_path, path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'svc.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/<int:to_user_id>/<str:room_name>', consumers.ChatConsumer.as_asgi()),
        ])
    ),
})
