from django.urls import path, include
from .views import DashboardView, AllUsersView, AllCusView, AllProView, AddAll

app_name = 'admins'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('allusers/', AllUsersView.as_view(), name='allusers'),
    path('allclients/', AllCusView.as_view(), name='allcus'),
    path('allprofessionals/', AllProView.as_view(), name='allpro'), 
    path('addall/', AddAll.as_view(), name='addall')
]