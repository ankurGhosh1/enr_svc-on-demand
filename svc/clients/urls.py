from django.urls import path, include
from . import views
from .views import JobPostView, GetJobPost, JobDetailView, JobUpdateView, getSubCats, getCats

app_name = 'clients'

urlpatterns = [
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('jobpost/', JobPostView.as_view(), name="jobpost"),
    path('alljobs/', GetJobPost.as_view(), name="alljobs"),
    path('alljobs/<int:pk>/', JobDetailView.as_view(), name="jobdetail"),
    path('alljobs/<int:pk>/update', JobUpdateView.as_view(), name="jobupdate"),
    path('get/subcats', getSubCats, name="getSubCats"),
    path('get/cats', getCats, name="getCats"),
    path('profile/',views.MyProfile,name = 'profile'),
    
]
