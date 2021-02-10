from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import SignupView, HomeView # JobPostingView, AllJobView, chat, JobUpdateView, JobDetailView, JobDeleteView

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('signup/', SignupView.as_view(), name = 'signup'),
    # path('login/', LoginView.as_view(), name="login"),
    # path('reset-password/', PasswordResetView.as_view(), name="reset_password"),
    # path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # path('logout/', LogoutView.as_view(), name="logout"),
    # path('jobpost/', JobPostingView.as_view(), name="jobpost"),
    # path('jobpost/<int:pk>', JobDetailView.as_view(), name="jobdetail"),
    # path('jobpost/<int:pk>/update', JobUpdateView.as_view(), name="jobupdate"),
    # path('jobpost/<int:pk>/delete', JobDeleteView.as_view(), name="jobdelete"),
    # path('alljobs/', AllJobView.as_view(), name="alljobs"),
    # path('chat/<str:user_id>', chat, name="chat")
]
