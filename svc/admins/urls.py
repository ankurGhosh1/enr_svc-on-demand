from django.urls import path, include
from .views import DashboardView, AllUsersView, AllCusView, AllProView, AddAll, AddSubCategory, AllAdminView, AllStaffView, AddCountryView, DeleteCountryView, DeleteCategoryView, DeleteSubCategoryView 

app_name = 'admins'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('allusers/', AllUsersView.as_view(), name='allusers'),
    path('allclients/', AllCusView.as_view(), name='allcus'),
    path('allprofessionals/', AllProView.as_view(), name='allpro'), 
    path('addall/', AddAll.as_view(), name='addall'),
    path('addsub/', AddSubCategory.as_view(), name='addsub'),
    path('alladmin/', AllAdminView.as_view(), name='alladmin'),
    path('allstaff/', AllStaffView.as_view(), name='allstaff'),
    path('addcountry/', AddCountryView.as_view(), name='addcon'),
    path('deletecountry/<int:pk>', DeleteCountryView.as_view(), name='deletecon'),
    path('deletecategory/<int:pk>', DeleteCategoryView.as_view(), name='deletecat'),
    path('deletesubcategory/<int:pk>', DeleteSubCategoryView.as_view(), name='deletesubcat')
]