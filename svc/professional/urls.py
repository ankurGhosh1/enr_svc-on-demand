from django.urls import path, include
# from .views import SignupView, HomeView, JobPostingView, AllJobView, chat
from . import views
app_name = 'professional'

urlpatterns = [
    path('proffessional/profile',views.profile,name = 'profile'),
]
