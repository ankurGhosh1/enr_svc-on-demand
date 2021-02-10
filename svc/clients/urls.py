from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# from .views import SignupView, HomeView, JobPostingView, MyJobView, chat, IndiJobView, JobUpdateView, JobDetailView, JobDeleteView
from .views import HomeView
app_name = 'clients'

urlpatterns = [
    # path('', HomeView.as_view(), name="home"),
    # path('signup/', SignupView.as_view(), name = 'signup'),
    # path('login/', LoginView.as_view(), name="login"),
    # path('reset-password/', PasswordResetView.as_view(), name="reset_password"),
    # path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # path('logout/', LogoutView.as_view(), name="logout"),
    # path('jobpost/', JobPostingView.as_view(), name="jobpost"),
    # path('myjobs/', MyJobView.as_view(), name="myJobs"),
    # path('myjobs/<int:job_id>', IndiJobView.as_view(), name="indiJob"),
    # path('chat/<str:user_id>', chat, name="chat"),
    # path('jobpost/<int:pk>', JobDetailView.as_view(), name="jobdetail"),
    # path('jobpost/<int:pk>/update', JobUpdateView.as_view(), name="jobupdate"),
    # path('jobpost/<int:pk>/delete', JobDeleteView.as_view(), name="jobdelete"),






    path('', HomeView.as_view(), name="signup"),
    path('', HomeView.as_view(), name="login"),
    path('', HomeView.as_view(), name="reset_password"),
    path('', HomeView.as_view(), name="password_reset_done"),
    path('', HomeView.as_view(), name="password_reset_confirm"),
    path('', HomeView.as_view(), name="password_reset_complete"),
    path('', HomeView.as_view(), name="logout"),
    path('', HomeView.as_view(), name="jobpost"),
    path('', HomeView.as_view(), name="myJobs"),
    path('', HomeView.as_view(), name="indiJob"),
    path('', HomeView.as_view(), name="chat"),
    path('', HomeView.as_view(), name="jobdetail"),
    path('', HomeView.as_view(), name="jobupdate"),
    path('', HomeView.as_view(), name="jobdelete"),
]
