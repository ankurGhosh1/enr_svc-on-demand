from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.db import connection
from django.core.paginator import Paginator
from clients.forms import CategoryForm, SubCategoryForm, CountryForm, StateForm, CityForm
from svc.utils import AllProcedures
import datetime

# Create your views here.

def groupIT(key, lis):
    gs_dict = {}
    gs = []
    group = []
    for i in lis:
        if i[key] not in gs_dict:
            gs_dict[i[key]] = [i]
        else:
            gs_dict[i[key]].append(i)
    for i in gs_dict:
        gs.append(gs_dict[i])

    return gs


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class DashboardView(View):
    def get(self, request):
        print(request.user.id)
        return render (request, 'admins/dashboard.html')


class AllUsersView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminGetAllUser")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 1)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        print(alluser)
        return render(request, 'admins/allusers.html', {'allusers': allusers})

class AllCusView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminGetAllClient")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 1)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        print(alluser)
        return render(request, 'admins/allusers.html', {'allusers': allusers})


class AllProView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminGetAllProfessional")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 1)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        print(alluser)
        return render(request, 'admins/allusers.html', {'allusers': allusers})

class AddAll(View):
    def get(self, request):
        categoryform = CategoryForm
        subcategoryform = SubCategoryForm
        countryform = CountryForm
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminAllCountry")
        allcon = dictfetchall(cursor)
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminAllCategory")
        allcategory = dictfetchall(cursor)
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminAllsubCategory")
        allsubcategory = dictfetchall(cursor)
        print(allsubcategory)
        gc = groupIT('City', allcategory)
        context = {
            'grouped_category':gc,
            'categoryform': categoryform,
            'subcategoryform': subcategoryform,
            'countryform': countryform,
            'allcon': allcon,
            'allcategory': allcategory,
            'allsubcategory': allsubcategory
            }
        return render(request, 'admins/create.html', context)

    def post(self, request):
        if request.method == 'POST':
            _id = request.user.id
            categoryName = request.POST['CategoryName']
            city_id = request.POST['city_id']
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.createCategory @CategoryName='{categoryName}', @AddedBy='{_id}', @AddedDate='{datetime.datetime.now()}', @IsActive='{1}' ")
            id = cursor.execute('SELECT @@IDENTITY AS [@@IDENTITY];')
            print(id)
            id = id.fetchall()
            cat_id = id[0][0]
            AllProcedures.addCatInCity(cat_id, city_id)
            return redirect('/staff/addall')


class DeleteCategoryView(View):
    def get(self, request, pk):
        _id = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.deleteCategory @id='{_id}'")
        return redirect('/staff/addall')

class DeleteSubCategoryView(View):
    def get(self, request, pk):
        _id = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.deleteSubCategory @id='{_id}'")
        return redirect('admins:addcon')


class AddSubCategory(View):
    def post(self, request):
        if request.method == 'POST':
            _id = request.user.id
            subcategory = request.POST['SubCategoryName']
            category = request.POST['Category']
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.createSubCategory @SubCategoryName='{subcategory}', @Category='{category}', @AddedBy='{_id}', @AddedDate='{datetime.datetime.now()}', @IsActive='{1}' ")
            return redirect('/staff/addall')


class AddCountryView(View):
    def get(self, request):

        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminAllCountry")
        allcon = dictfetchall(cursor)
        countryform = CountryForm
        context = {
            'allcon': allcon,
            'countryform': countryform,
            }
        return render(request, 'admins/createCountry.html', context)


    def post(self, request):
        if request.method == 'POST':
            country = request.POST['Country']
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.createCountry @Country='{country}', @IsActive='{1}' ")
            return redirect('admins:addcon')


class DeleteCountryView(View):
    def get(self, request, pk):
        _id = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.deleteCountry @id='{_id}'")
        return redirect('admins:addcon')



class AddStateView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminGetState")
        states = dictfetchall(cursor)
        stateFrom = StateForm
        gs = groupIT('CountryName', states)
        print(gs)
        context = {
            'grouped_states': gs,
            'stateFrom': StateForm,
            }
        return render(request, 'admins/createState.html', context)


    def post(self, request):
        if request.method == 'POST':
            country = request.POST['CountryId']
            state = request.POST['State']
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.createState @country_id='{country}', @IsActive='{1}', @state='{state}'")
            return redirect('admins:addstate')



class AddSubCatView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminAllCountry")
        allcon = dictfetchall(cursor)
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminAllSubCategory")
        allsubcategory = dictfetchall(cursor)
        allsubcats = groupIT('CategoryName', allsubcategory)
        print(allsubcats)
        context = {
            'allcon': allcon,
            'grouped_subCats': allsubcats
            }
        return render(request, 'admins/createSubCat.html', context)


    def post(self, request):
        if request.method == 'POST':
            _id = request.user.id
            subCategoryName = request.POST['SubCategoryName']
            city_id = request.POST['city_id']
            category_id = request.POST['category_id']
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.createSubCategory @SubCategoryName='{subCategoryName}',@cat_id='{category_id}', @AddedBy='{_id}', @AddedDate='{datetime.datetime.now()}', @IsActive='{1}' ")
            return redirect('admins:addsubcat')





class AddCityView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminGetCity")
        cities = dictfetchall(cursor)
        cityForm = CityForm
        gs = groupIT('StateName', cities)
        print(gs)
        context = {
            'grouped_states': gs,
            'cityForm': CityForm,
            }
        return render(request, 'admins/createCity.html', context)


    def post(self, request):
        if request.method == 'POST':
            state = request.POST['StateId']
            city = request.POST['City']
            Latitude = request.POST['Latitude']
            Longitude = request.POST['Longitude']
            user_id = request.user.id
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.createCity @state_id='{state}', @lat='{Latitude}', @log='{Longitude}', @IsActive='{1}', @city='{city}', @addedDate='{datetime.datetime.now()}', @addedby_id='{user_id}'")
            return redirect('admins:addcity')



class DeleteCityView(View):
    def get(self, request, city_id):
        _id = self.kwargs.get('city_id')
        cursor = connection.cursor()

        cursor.execute(f"EXEC dbo.deleteCity @id='{_id}'")
        return redirect('admins:addcity')




class DeleteStateView(View):
    def get(self, request, state_id):
        _id = self.kwargs.get('state_id')
        cursor = connection.cursor()

        cursor.execute(f"EXEC dbo.deleteState @id='{_id}'")
        return redirect('admins:addstate')




class ActivateStateView(View):
    def get(self, request, state_id):
        _id = self.kwargs.get('state_id')
        cursor = connection.cursor()

        cursor.execute(f"EXEC dbo.activateState @id='{_id}'")
        return redirect('admins:addstate')

class ActivateCityView(View):
    def get(self, request, city_id):
        _id = self.kwargs.get('city_id')
        cursor = connection.cursor()

        cursor.execute(f"EXEC dbo.activateCity @id='{_id}'")
        return redirect('admins:addcity')



class ActivateCatView(View):
    def get(self, request, cat_id):
        _id = self.kwargs.get('cat_id')
        cursor = connection.cursor()

        cursor.execute(f"EXEC dbo.activateCat @id='{_id}'")
        return redirect('admins:addall')


class ActivateSubCatView(View):
    def get(self, request, subcat_id):
        _id = self.kwargs.get('subcat_id')
        cursor = connection.cursor()

        cursor.execute(f"EXEC dbo.activateSubCat @id='{_id}'")
        return redirect('admins:addsubcat')


class DeleteCountryView(View):
    def get(self, request, pk):
        _id = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.deleteCountry @id='{_id}'")
        return redirect('admins:addcon')

class ActivateConView(View):
    def get(self, request, pk):
        _id = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.activateCountry @id='{_id}'")
        return redirect('admins:addcon')



class DeleteCatView(View):
    def get(self, request, cat_id):
        _id = self.kwargs.get('cat_id')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.deleteCat @id='{_id}'")
        return redirect('admins:addall')


class DeleteSubCatView(View):
    def get(self, request, subcat_id):
        _id = self.kwargs.get('subcat_id')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.deleteSubCat @id='{_id}'")
        return redirect('admins:addsubcat')


class AllAdminView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminGetAllAdmin")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 1)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        print(alluser)
        return render(request, 'admins/allusers.html', {'allusers': allusers})


class AllStaffView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AdminGetAllStaff")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 1)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        print(alluser)
        return render(request, 'admins/allusers.html', {'allusers': allusers})
