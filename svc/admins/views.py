from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.db import connection
from django.core.paginator import Paginator
from clients.forms import CategoryForm, SubCategoryForm, CountryForm
import datetime

# Create your views here.

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
        cursor.execute(f"EXEC dbo.getAllUser")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 9)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        # print(alluser) 
        return render(request, 'admins/allusers.html', {'allusers': allusers})

class AllCusView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getAllClient")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 9)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        # print(alluser) 
        return render(request, 'admins/allusers.html', {'allusers': allusers})


class AllProView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getAllProfessional")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 9)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        # print(alluser) 
        return render(request, 'admins/allusers.html', {'allusers': allusers})

class AddAll(View):
    def get(self, request):
        categoryform = CategoryForm
        subcategoryform = SubCategoryForm
        countryform = CountryForm
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.AllCountry")
        allcon = dictfetchall(cursor)
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.allCategory")
        allcategory = dictfetchall(cursor)
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.allsubCategory")
        allsubcategory = dictfetchall(cursor)
        context = {
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
            category = request.POST['CategoryName']
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.createCategory @CategoryName='{category}', @AddedBy='{_id}', @AddedDate='{datetime.datetime.now()}', @IsActive='{1}' ")
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
        return redirect('/staff/addall')


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
    def post(self, request):
        if request.method == 'POST':
            country = request.POST['Country']
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.createCountry @Country='{country}', @IsActive='{1}' ")
            return redirect('/staff/addall')

# Delete Country View

class DeleteCountryView(View):
    def get(self, request, pk):
        _id = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.deleteCountry @id='{_id}'")
        return redirect('/staff/addall')

# Admin View

class AllAdminView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getAllAdmin")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 9)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        print(alluser) 
        return render(request, 'admins/allusers.html', {'allusers': allusers})

# Staff View

class AllStaffView(View):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getAllStaff")
        alluser = dictfetchall(cursor)
        paginator = Paginator(alluser, 9)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        # print(alluser) 
        return render(request, 'admins/allusers.html', {'allusers': allusers})
