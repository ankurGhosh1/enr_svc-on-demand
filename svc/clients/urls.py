from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignupView, HomeView, JobPostingView, AllJobView, chat

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('signup/', SignupView.as_view(), name = 'signup'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('jobpost/', JobPostingView.as_view(), name="jobpost"),
    path('alljobs/', AllJobView.as_view(), name="alljobs"),
    path('chat/<str:user_id>', chat, name="chat")
]
