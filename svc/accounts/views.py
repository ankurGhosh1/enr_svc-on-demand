from django.shortcuts import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from collections import namedtuple
import datetime
cursor = connection.cursor()
# Create your views here.
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
           proffessional = cursor.execute("SELECT count(*) FROM baghiService.dbo.accounts_userlist WHERE UserType_id = 1 AND email = %s AND phone = %s",[email, password]).fetchone()[0]
           consumers = cursor.execute("SELECT count(*) FROM baghiService.dbo.accounts_userlist WHERE UserType_id = 2 AND email = %s AND phone = %s",[email, password]).fetchone()[0]
           try:
              if(consumers == 1):
                 request.session['email'] = email
                 return redirect('clients:profile')
           except ObjectDoesNotExist:
              if (proffessional == 1):
                 request.session['email'] = email
                 return redirect('professional:profile')
        except ObjectDoesNotExist:
            return redirect('accounts:login')

    return render(request,'registration/login.html')

def signup(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM baghiService.dbo.accounts_usertype")
    user_t = dictfetchall(cursor)

    cursor.execute("SELECT * FROM baghiService.dbo.accounts_applcationlist")
    app = dictfetchall(cursor)

    if request.method == 'POST':
        li = []
        for i in request.POST:
            if i!='csrfmiddlewaretoken':
                li.append(request.POST[i])
        query = f"EXEC [dbo].[addUser]  @first_name = '{li[0]}', @last_name = '{li[1]}', @email = '{li[2]}', @ContactCell = '{li[3]}', @password = '{li[4]}', @UserTypeId = '{li[5]}', @ApplicationId = '{li[6]}', @date_joined='{datetime.datetime.now()}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
        return redirect('accounts:signup')
    return render(request,'registration/signup.html',{'user_type':user_t,'application':app})


def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return redirect('clients:login')
