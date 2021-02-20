from django.urls import path, include
# from .views import SignupView, HomeView, JobPostingView, AllJobView, chat
from . import views
app_name = 'professional'

urlpatterns = [
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('profile/',views.MyProfile,name = 'profile'),
    path('explore/',views.Explore,name = 'explore'),
    path('indiJob/<int:job_id>',views.indiJob,name = 'indiJob'),
]
