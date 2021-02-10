from django.urls import path, include
<<<<<<< HEAD
# from .views import SignupView, HomeView, JobPostingView, AllJobView, chat
from . import views
app_name = 'accounts'

urlpatterns = [
    path('',views.login,name = 'login'),
    path('signup',views.signup,name ='signup'),
    path('logout',views.logout,name ='logout'),
=======
from .views import HomeView

app_name = 'accounts'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
>>>>>>> 1063b8785d20a292866d9d196df172530257f046
]
