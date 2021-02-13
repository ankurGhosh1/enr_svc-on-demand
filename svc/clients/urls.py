from django.urls import path, include
from . import views
from .views import JobPostView, GetJobPost, JobDetailView, JobUpdateView

app_name = 'clients'

urlpatterns = [
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('jobpost/', JobPostView.as_view(), name="jobpost"),
    path('alljobs/', GetJobPost.as_view(), name="alljobs"),
    path('alljobs/<int:pk>/', JobDetailView.as_view(), name="jobdetail"),
    path('alljobs/<int:pk>/update', JobUpdateView.as_view(), name="jobupdate"),
    # path('myjobs/', MyJobView.as_view(), name="myJobs"),
    # path('myjobs/<int:job_id>', IndiJobView.as_view(), name="indiJob"),
    # path('chat/<str:user_id>', views.chat, name="chat"),
    # path('jobpost/<int:pk>/delete', JobDeleteView.as_view(), name="jobdelete"),

]
