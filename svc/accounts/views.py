from django.shortcuts import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from collections import namedtuple
from svc.utils import AllProcedures
from django.contrib.auth.hashers import make_password, check_password
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
        user = AllProcedures.getUserWithEmail(email)
        print(user, "user")
        try:
            if check_password(password, user[1]):
                request.session['user'] = {
                'is_authenticated': True,
                'id':user[0],
                'email':user[4],
                'info': user[2:10]+user[11:]
                }
                if(user[-1]==2):
                    request.session['user']['type'] = "Client"
                    return redirect('clients:profile')
                if (user[-1]==1):
                    request.session['user']['type'] = "Professional"
                    return redirect('professional:profile')
        except ObjectDoesNotExist:
            return redirect('accounts:login')
    print(request.session.get('user'), "all user session")
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
            if i=="password":
                hashed = make_password(request.POST[i])
                li.append(hashed)
            elif i!='csrfmiddlewaretoken':
                li.append(request.POST[i])
        saved = AllProcedures.createUser(li)
        return redirect('accounts:login')
    return render(request,'registration/signup.html',{'user_type':user_t,'application':app})


def logout(request):
    try:
        del request.session['user']
    except:
        pass
    return redirect('accounts:login')