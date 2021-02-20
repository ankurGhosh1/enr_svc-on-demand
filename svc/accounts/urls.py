from django.urls import path, include

# from .views import SignupView, HomeView, JobPostingView, AllJobView, chat
from . import views
app_name = 'accounts'

urlpatterns = [
    path('',views.home,name = 'home'),
    path('login/',views.login,name = 'login'),
    path('signup/',views.signup,name ='signup'),
    path('logout/',views.logout,name ='logout'),
    path('social/logedin/',views.s_login,name ='social_login'),
    path('complete/google-oauth2/',views.s_complete,name ='social_complete'),
    path('complete/facebook/',views.f_complete,name ='social_complete'),
    path('complete/typeSelection',views.selectUserType,name ='selectusertype'),
    path('address_add/',views.addressAdd,name ='address_add'),
    path('update_profile/',views.update_profile,name ='update_profile'),
    path('password_change/',views.password_change,name ='password_change'),
    path('password_reset_form/',views.password_reset_form,name ='password_reset_form'),
    path('password_reset_otp/',views.password_reset_otp,name ='password_reset_otp'),
    path('password_reset_confirm/',views.password_reset_confirm,name ='password_reset_confirm'),
    path('password_reset_done/',views.password_reset_complete,name ='password_reset_complete')
]
