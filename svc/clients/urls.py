from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import SignupView, HomeView, JobPostingView, AllJobView, chat

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('signup/', SignupView.as_view(), name = 'signup'),
    path('login/', LoginView.as_view(), name="login"),
    path('password-reset/', PasswordResetView.as_view(), name="password-reset"),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('jobpost/', JobPostingView.as_view(), name="jobpost"),
    path('alljobs/', AllJobView.as_view(), name="alljobs"),
    path('chat/<str:user_id>', chat, name="chat")
]
