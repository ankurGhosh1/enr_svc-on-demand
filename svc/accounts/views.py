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


BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def home(request):
    if request.session.has_key('user'):
        if request.session['user']['type']:
            if request.session['user']['type'] == "Client":
                return redirect(f'client:dashboard')

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
