from django.shortcuts import *
from svc.utils import AllProcedures

def profile(request):
    user = AllProcedures.getUserWithId(request.session['user']['id'])
    return render(request, 'professional/profile.html', {'profile': user})
