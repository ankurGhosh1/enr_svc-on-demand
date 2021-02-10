"""
ASGI config for svc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
# from svc import consumers
from django.urls import re_path, path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'svc.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # re_path(r'ws/chat/(?P<to_user_id>[0-9]+)/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
            # path('ws/chat/<int:to_user_id>/<str:room_name>', consumers.ChatConsumer.as_asgi()),
        ])
    ),
})
