from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from svc.utils import AllProcedures, FastProcedures, dictfetchall






def dashboard(request):
    cursor = connection.cursor()
    address = cursor.execute("SELECT COUNT(*) FROM testenr.dbo.accounts_addresslist WHERE user_id = %s", [request.session['user']['id']]).fetchone()[0]
    if address == 0 :
        return redirect('accounts:address_add')
    return render(request, 'professional/dashboard.html')


def Explore(request):
    nearJobs = AllProcedures.getMyCityJobs(user_id=request.session['user']['id'])

    return render(request, 'professional/explore.html', {'jobs':nearJobs})

def indiJob(request, job_id):

    cursor = connection.cursor()
    cursor.execute(f"EXEC dbo.getEachJob @id='{job_id}'")
    eachjob = dictfetchall(cursor)
    return render(request, 'professional/indiJob.html', {'jobdetail': eachjob})


def MyProfile(request):
    return render(request, 'professional/myprofile.html')
