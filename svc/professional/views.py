from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection






def dashboard(request):
    cursor = connection.cursor()
    address = cursor.execute("SELECT COUNT(*) FROM baghiService.dbo.accounts_addresslist WHERE user_id = %s", [request.session['user']['id']]).fetchone()[0]
    if address == 0 :
        return redirect('accounts:address_add')
    return render(request, 'professional/dashboard.html')



def MyProfile(request):
    return render(request, 'professional/myprofile.html')
