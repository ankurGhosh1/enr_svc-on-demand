from django.urls import path, include
from . import views

app_name = 'chatApp'

urlpatterns = [
    path('chat/<str:user_id>', views.chat, name="chat"),
    path('chat/', views.chatApp, name="chatApp"),
]
