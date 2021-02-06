from django.urls import path, include
# from .views import SignupView, HomeView, JobPostingView, AllJobView, chat

app_name = 'professional'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('allquotes/', AllQuotes, name="allQuotes")
]
