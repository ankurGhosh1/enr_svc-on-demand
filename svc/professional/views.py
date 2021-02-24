from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from svc.utils import AllProcedures, FastProcedures, dictfetchall






def dashboard(request):
    cursor = connection.cursor()
    address = cursor.execute("SELECT COUNT(*) FROM baghiService.dbo.accounts_addresslist WHERE user_id = %s", [request.session['user']['id']]).fetchone()[0]
    if address == 0 :
        return redirect('accounts:address_add')
    return render(request, 'professional/dashboard.html')


def Explore(request):
    if request.session.has_key('user'):
        nearJobs = AllProcedures.getMyCityJobs(user_id=request.session['user']['id'])
        print(nearJobs)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM baghiService.dbo.accounts_citylist")
        city = dictfetchall(cursor)
        appliedList = []
        user_id = request.session['user']['id']
        appliedList = AllProcedures.getAppliedJobsList(user_id)
        print(appliedList)
        return render(request, 'professional/explore.html', {'jobs':nearJobs, 'city':city, 'appliedList':appliedList})
    return redirect('accounts:login')


def filter(request):
    if request.method=="POST":
        city = request.POST['city']
        cat = request.POST['cat']
        subCat = request.POST['subCat']
        print(city, cat, subCat)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM baghiService.dbo.accounts_citylist")
        cities = dictfetchall(cursor)
        jobs = AllProcedures.getFilterJobs(city_id=city, subcat_id=subCat, cat_id=cat)
        if request.session.has_key('user'):
            user_id = request.session['user']['id']
            appliedList, appliedJobs = AllProcedures.getAppliedJobsList(user_id)
        return render(request, 'professional/explore.html', {'jobs':jobs, 'city':cities, 'appliedList':appliedList})
    return HttpResponse(f"heheheh-{city}-{cat}-{subCat}")


def Applied(request):
    appliedList = []
    if request.session.has_key('user'):
        user_id = request.session['user']['id']
        appliedList, appliedJobs = AllProcedures.getAppliedJobsList(user_id)
        print(appliedList)
        script = '''
            <script>
                document.getElementById('page-heading').innerHTML = "Applied Jobs";
                var k = document.getElementById('filter_button');
                k.parentNode.removeChild(k);
            </script>
        '''
        return render(request, 'professional/explore.html', {'jobs':appliedJobs, 'appliedList':appliedList, 'script':script})
    return redierct('accounts:login')




def indiJob(request, job_id):

    cursor = connection.cursor()
    cursor.execute(f"EXEC dbo.getEachJob @id='{job_id}'")
    eachjob = dictfetchall(cursor)
    id = eachjob[0]['User_id']
    cursor = connection.cursor()
    cursor.execute(f"EXEC dbo.getUserWithId @id='{id}'")
    user = dictfetchall(cursor)
    appliedList = []
    if request.session.has_key('user'):
        user_id = request.session['user']['id']
        appliedList, appliedJobs = AllProcedures.getAppliedJobsList(user_id)
    applied = False
    if job_id in appliedList:
        applied = True
    return render(request, 'professional/indiJob.html', {'jobdetail': eachjob, 'user':user[0], 'applied':applied})


def applyJob(request, job_id):
    if request.session.has_key('user'):
        user_id = request.session['user']['id']
        appliedList = AllProcedures.getAppliedJobsList(user_id)
        applied = False
        user_id = request.session['user']['id']
        if job_id not in appliedList:
            AllProcedures.applyJob(user_id, job_id)
        return redirect('professional:indiJob', job_id=job_id)
    return redirect('accounts:signup')




def MyProfile(request):
    return render(request, 'professional/myprofile.html')
