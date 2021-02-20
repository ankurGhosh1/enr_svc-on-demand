from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from collections import namedtuple
from svc.utils import AllProcedures
from django.contrib.auth.hashers import make_password, check_password
import datetime
import requests as re
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from django.db import connection
from django.conf import settings
import os
from django.contrib import messages
import random, string
from django.core.mail import send_mail


BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def home(request):
    if request.session.has_key('user'):
        if request.session['user']['type']:
            if request.session['user']['type'] == "Client":
                return redirect(f'clients:dashboard')

            if request.session['user']['type'] == "Professional":
                return redirect(f'professional:dashboard')

    return render(request, 'home.html')

def _login(request, user, password, pass_req):
    if check_password(password, user[1]) or pass_req:
        request.session['user'] = {
        'is_authenticated': True,
        'id':user[0],
        'email':user[4],
        'info': user[2:10]+user[11:]
        }
        type = AllProcedures.getUserType(user[-1])
        print(type)
        if(type and type[0]=="Customer"):
            request.session['user']['type'] = "Client"
            return redirect('clients:dashboard')
        elif not type:
            return redirect('accounts:login')
        else:
            request.session['user']['type'] = "Professional"
            return redirect('professional:dashboard')
    return redirect('accounts:login')

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


def s_login(request):
    return HttpResponse(f"test signup {request.__dict__}")

def s_complete(request):
    state = request.GET.get('state')
    # scope = ["https://www.googleapis.com/auth/userinfo.email.read", " https://www.googleapis.com/auth/userinfo.profile"]
    code = request.GET.get('code')
    prompt = request.GET.get('prompt')
    request.session['user'] = {}
    request.session['user']['state'] = state
    flow = Flow.from_client_secrets_file(
    BASE+'/accounts/client_secret.json',
    scopes=None,
    state=state)
    flow.redirect_uri = f'{settings.HOST}/complete/google-oauth2/'
    try:
        req_state =request.META['QUERY_STRING'] if "state" in request.META['QUERY_STRING'] else request.scope['query_string']
    except:
        req_state = None
    print(req_state)

    print(state, code, prompt, sep="\n")
    authorization_response = request.get_raw_uri()
    if state in str(req_state):
        flow.fetch_token(authorization_response=authorization_response)
        credentials = flow.credentials
        service = build('people', 'v1', credentials=credentials)
        profile = service.people().get(resourceName='people/me', personFields='emailAddresses').execute()
        print(profile)
        user = AllProcedures.getUserWithEmail(profile['emailAddresses'][0]['value'])
        if user:
            return _login(request, user, "a", True)
        request.session['user']['email'] = profile['emailAddresses'][0]['value']
    return redirect("accounts:selectusertype")

# def f_begin(request):
#     url = f"https://www.facebook.com/v9.0/dialog/oauth?response_type=token&display=popup&client_id={settings.SOCIAL_AUTH_FACEBOOK_KEY}&redirect_uri={settings.HOST}/complete/facebook/&auth_type=rerequest&scope=public_profile%2Cemail"
#     return HttpResponseRedirect(url)

def f_complete(request):
    state = request.GET.get('state')
    # scope = ["https://www.googleapis.com/auth/userinfo.email.read", " https://www.googleapis.com/auth/userinfo.profile"]
    code = request.GET.get('code')
    prompt = request.GET.get('prompt')
    request.session['user'] = {}
    request.session['user']['state'] = state
    print(state, code, prompt, request.__dict__)
    url = f'https://graph.facebook.com/v9.0/oauth/access_token?client_id={settings.SOCIAL_AUTH_FACEBOOK_KEY}&redirect_uri={settings.HOST}/complete/facebook/&client_secret={settings.SOCIAL_AUTH_FACEBOOK_SECRET}&code={code}'
    print(url)
    k = re.get(url)
    res = k.json()
    access_token = res['access_token']
    url = f'https://graph.facebook.com/me?fields=id,name,email&access_token={access_token}'
    k = re.get(url)
    res = k.json()
    request.session['user'] = {'email':res['email']}
    user = AllProcedures.getUserWithEmail(res['email'])
    if user:
        return _login(request, user, "a", True)
    return redirect("accounts:selectusertype")

def selectUserType(request):
    cursor.execute("SELECT * FROM baghiService.dbo.accounts_appliationlist")
    app = dictfetchall(cursor)
    if request.method=='POST':
        type = request.POST.get('userType');
        print(type)
        if type in ['Professional', 'Customer']:
            li = []
            for i in request.POST:
                if i=="password":
                    hashed = make_password(request.POST[i])
                    li.append(hashed)
                elif i!='csrfmiddlewaretoken':
                    li.append(request.POST[i])
            li = li[0:2]+[request.session['user']['email']]+li[2:]
            print(li)
            AllProcedures.createUserWithType(li)
        user = AllProcedures.getUserWithEmail(request.session['user']['email'])
        if user:
            return _login(request, user, "a", True)
    return render(request, 'registration/selectType.html', {'application':app})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = AllProcedures.getUserWithEmail(email)
        if user:
            return _login(request, user, password, False)
        return redirect('accounts:login')
    print(request.session.get('user'), "all user session")
    return render(request,'registration/login.html')

def signup(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM baghiService.dbo.accounts_usertype")
    user_t = dictfetchall(cursor)

    cursor.execute("SELECT * FROM baghiService.dbo.accounts_appliationlist")
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




def addressAdd(request):
    country = AllProcedures.getCountry()
    state = AllProcedures.getState()
    city = AllProcedures.getCityByState()
    print(country, state, city)
    if request.method == 'POST':
        li = []
        for i in request.POST:
            if i!='csrfmiddlewaretoken':
                li.append(request.POST[i])
                li.append(request.session['user']['id'])
        print(li)
        saved = AllProcedures.addressAddUser(li)
        print(li)
        user = AllProcedures.getUserWithEmail(request.session['user']['email'])
        type = AllProcedures.getUserType(user[-1])
        if (type and type[0] == "Customer"):
            return redirect('clients:dashboard')
        elif (type and type[0] == "Professional"):
            return redirect('professional:dashboard')
    print(AllProcedures.getAddressList())
    return render(request,'address_add.html',{'country':country,'state':state,'city':city})



def update_profile(request):
    country = AllProcedures.getCountry()
    state = AllProcedures.getState()
    city = AllProcedures.getCityByState()
    address = AllProcedures.getUserAddress(request.session['user']['id'])
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM baghiService.dbo.accounts_appliationlist")
        app = dictfetchall(cursor)
    with connection.cursor() as cursor:
        cursor.execute(f"EXEC dbo.getUserWithId @id='{request.session['user']['id']}'")
        user = namedtuplefetchall(cursor)
    if request.method == 'POST':
        li = []
        for i in request.POST:
            if i!='csrfmiddlewaretoken':
                li.append(request.POST[i])
        user_id = user[0].id
        saved = AllProcedures.updateUser(li,user_id)
        print(li)
        return redirect('professional:profile')
    return render(request,'update_profile.html',{'user':user,'application':app,'country':country,'state':state,'city':city,'address':address})



def password_change(request):
    with connection.cursor() as cursor:
        cursor.execute(f"EXEC dbo.getUserWithId @id='{request.session['user']['id']}'")
        user = namedtuplefetchall(cursor)
        print(user)

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if check_password(old_password, user[0].password):
            if new_password == confirm_password:
                password = make_password(new_password)
                saved = AllProcedures.userPasswordChange(password, user[0].id)
                del request.session['user']
                return redirect('accounts:login')
            else:
                messages.error(request, 'Your new and confirm password not matched!')
                return redirect('accounts:password_change')
        else:
            messages.error(request, 'Your old password is incorrect!')
            return redirect('accounts:password_change')
    return render(request,'password_change.html')


def password_reset_form(request):
    if request.session.has_key('user'):
        del request.session['user']
    if request.session.has_key('otp'):
        del request.session['otp']

    otp = ''.join(random.choices(string.digits, k=6))
    email = request.POST.get('email')
    with connection.cursor() as cursor:
        users = cursor.execute("SELECT COUNT(*) FROM baghiService.dbo.accounts_userlist WHERE email = %s",[email]).fetchone()[0]
    if request.method == 'POST':
        if users == 1:
            saved = AllProcedures.generateOTP(otp,email)
            subject = "Password Reset"
            message = f"Someone can try to  reset your password\nEmail: {email} \nYour OTP: {otp}"
            sender = "pkkapoor98@gmail.com"
            send_mail(subject, message, sender, [email])
            request.session['otp'] = email
            return redirect('accounts:password_reset_otp')
        else:
            messages.error(request, 'Your register email not matched!')
            return redirect('accounts:password_reset_form')
    return render(request,'registration/password_reset_form.html')

def password_reset_otp(request):
    if not request.session.has_key('otp'):
        return redirect('accounts:password_reset_form')
    with connection.cursor() as cursor:
        cursor.execute("SELECT TOP 1 * FROM baghiService.dbo.accounts_otp WHERE user_email = %s ORDER BY id DESC", [request.session['otp']])
        otp = namedtuplefetchall(cursor)
    minute_count = round((datetime.datetime.now()-otp[0].doc).total_seconds() / 60)
    if request.method == 'POST':
        otp_get = request.POST.get('otp')
        if(otp[0].Otp == otp_get and minute_count <= int(otp[0].expire_minute)):
            return redirect('accounts:password_reset_confirm')
        else:
            messages.error(request, 'You enter wrong otp or expire your otp!')
            return redirect('accounts:password_reset_otp')
    return render(request,'registration/password_reset_otp.html')

def password_reset_confirm(request):
    if not request.session.has_key('otp'):
        return redirect('accounts:password_reset_form')
    with connection.cursor() as cursor:
        cursor.execute(f"EXEC dbo.getUser @email='{request.session['otp']}'")
        user = namedtuplefetchall(cursor)
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            password = make_password(new_password)
            saved = AllProcedures.userPasswordChange(password, user[0].id)
            del request.session['otp']
            return redirect('accounts:password_reset_complete')
        else:
            messages.error(request, 'Your new and confirm password not matched!')
            return redirect('accounts:password_reset_confirm')
    return render(request,'registration/password_reset_confirm.html')

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')
