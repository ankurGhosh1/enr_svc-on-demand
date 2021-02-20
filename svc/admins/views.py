from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.db import connection
from django.core.paginator import Paginator

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
        paginator = Paginator(alluser, 1)
        page_number = request.GET.get('page')
        allusers = paginator.get_page(page_number)
        print(alluser)
        return render(request, 'admins/allusers.html', {'allusers': allusers})
