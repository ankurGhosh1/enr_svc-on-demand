from django.urls import path, include

# from .views import SignupView, HomeView, JobPostingView, AllJobView, chat
from . import views
app_name = 'accounts'

urlpatterns = [
    path('',views.login,name = 'login'),
    path('signup',views.signup,name ='signup'),
    path('logout',views.logout,name ='logout'),
]