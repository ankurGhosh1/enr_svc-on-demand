from django.urls import path, include
from .views import DashboardView, AllUsersView

app_name = 'admins'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('allusers/', AllUsersView.as_view(), name='allusers')
]