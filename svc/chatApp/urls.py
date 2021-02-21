from django.urls import path, include
from . import views

app_name = 'chatApp'

urlpatterns = [
    path('chat/<int:user_id>/<int:job_id>', views.chat, name="chat"),
    path('chat/', views.chatApp, name="chatApp"),
]
