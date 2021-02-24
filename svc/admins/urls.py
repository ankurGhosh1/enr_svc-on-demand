from django.urls import path, include
from .views import DashboardView, AllUsersView, AllCusView, AllProView, AddAll, AddSubCategory, AddSubCatView, AllAdminView, AddStateView, AllStaffView, AddCityView, AddCountryView, DeleteCityView, DeleteCategoryView, DeleteCountryView, DeleteStateView, DeleteSubCategoryView
from .import views
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
    path('addstate/', AddStateView.as_view(), name='addstate'),
    path('addcity/', AddCityView.as_view(), name='addcity'),
    path('addsubcat/', AddSubCatView.as_view(), name='addsubcat'),

    path('deletestate/<int:state_id>', DeleteStateView.as_view(), name='deletestate'),
    path('activatestate/<int:state_id>', views.ActivateStateView.as_view(), name='activate'),
    path('deletecity/<int:city_id>', DeleteCityView.as_view(), name='deletecity'),
    path('activatecity/<int:city_id>', views.ActivateCityView.as_view(), name='activateCity'),
    path('activatecon/<int:pk>', views.ActivateConView.as_view(), name='activatecon'),
    path('deletecountry/<int:pk>', DeleteCountryView.as_view(), name='deletecon'),
    path('activatecategory/<int:cat_id>', views.ActivateCatView.as_view(), name='activateCat'),
    path('deletecategory/<int:cat_id>', views.DeleteCatView.as_view(), name='deleteCat'),
    path('activatesubcategory/<int:subcat_id>', views.ActivateSubCatView.as_view(), name='activateSubCat'),
    path('deletesubcategory/<int:subcat_id>', views.DeleteSubCatView.as_view(), name='deleteSubCat'),
    path('deletesubcategory/<int:pk>', DeleteSubCategoryView.as_view(), name='deletesubcat')
]
