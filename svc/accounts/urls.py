from django.urls import path, include
from .views import HomeView

app_name = 'accounts'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
