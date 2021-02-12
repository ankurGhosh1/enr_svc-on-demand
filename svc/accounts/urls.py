from django.urls import path, include

# from .views import SignupView, HomeView, JobPostingView, AllJobView, chat
from . import views
app_name = 'accounts'

urlpatterns = [
    path('',views.login,name = 'login'),
    path('signup/',views.signup,name ='signup'),
    path('logout/',views.logout,name ='logout'),
    path('social/logedin/',views.s_login,name ='social_login'),
    path('complete/google-oauth2/',views.s_complete,name ='social_complete'),
    path('complete/facebook/',views.f_complete,name ='social_complete'),

    path('complete/typeSelection',views.selectUserType,name ='selectusertype'),
]
