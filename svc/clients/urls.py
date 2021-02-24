from django.urls import path, include
from . import views
from .views import JobPostView, GetJobPost, JobDetailView, JobUpdateView, JobDeleteView, AllProfessionals, Callback, Review , getSubCats, getCats, getStates, getCities

app_name = 'clients'

urlpatterns = [
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('jobpost/', JobPostView.as_view(), name="jobpost"),
    path('alljobs/', GetJobPost.as_view(), name="alljobs"),
    path('alljobs/<int:pk>/', JobDetailView.as_view(), name="jobdetail"),
    path('alljobs/<int:pk>/update', JobUpdateView.as_view(), name="jobupdate"),
    path('alljobs/<int:pk>/delete', JobDeleteView.as_view(), name="jobdelete"),
    path('services/', AllProfessionals.as_view(), name='services'),
    path('callback/<slug:slug>', Callback.as_view(), name='callback'),
    path('profile/<int:pk>', Review.as_view(), name='review'),
    path('get/subcats', getSubCats, name="getSubCats"),
    path('get/cats', getCats, name="getCats"),
    path('get/states', getStates, name="getStates"),
    path('get/cities', getCities, name="getCities"),
    path('profile/',views.MyProfile,name = 'profile'),
    # path('myjobs/', MyJobView.as_view(), name="myJobs"),
    # path('myjobs/<int:job_id>', IndiJobView.as_view(), name="indiJob"),
    # # path('chat/<str:user_id>', views.chat, name="chat"),
    # path('get/subcats', getSubCats, name="getSubCats"),
    # path('get/cats', getCats, name="getCats")
]
