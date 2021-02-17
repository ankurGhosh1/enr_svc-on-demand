from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.http import HttpResponse
from accounts.models import UserList
from .forms import JobPostForm, JobUpdateForm, AssetsForm
from django.views.generic import View
from django.db import connection
from svc.utils import AllProcedures, FastProcedures
from django.forms import inlineformset_factory
from accounts.models import TopicList, AssetsDetailList
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import datetime
from django.db import connection






def dashboard(request):
    cursor = connection.cursor()
    address = cursor.execute("SELECT COUNT(*) FROM baghiService.dbo.accounts_addresslist WHERE user_id = %s", [request.session['user']['id']]).fetchone()[0]
    if address == 0 :
        return redirect('accounts:address_add')
    return render(request, 'clients/dashboard.html')


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class JobPostView(generic.CreateView):
    assetForm = inlineformset_factory(TopicList, AssetsDetailList, AssetsForm, extra=1)
    def get(self, request):
        form_class = {'form': JobPostForm, 'assetsform': self.assetForm}
        return render(request, 'clients/jobposting.html', form_class)

    def post(self, request):
        if request.method == 'POST':
            li = []
            for i in request.POST:
                if i != 'csrfmiddlewaretoken':
                    li.append(request.POST[i])
                if 'assetsdetaillist_set' in i:
                    break
            folder = os.path.join(settings.MEDIA_ROOT, 'client')
            fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT
            query = ''
            now = datetime.datetime.now()
            user_id = request.session['user']['id']
            li.append(request.session['user']['id'])
            print(li)
            _, id = AllProcedures.createjob(li)
            print(id, request.FILES)
            for i in request.FILES:
                myfile = request.FILES[i]
                filename = fs.save(myfile.name, myfile)
                ext = myfile.name.split(".")[-1]
                file_url = fs.url(filename)
                values = {
                    'file_name':folder+file_url,
                    'file_ext':ext,
                    'added_date':now,
                    'updated_date':now,
                    'addedby_id':user_id,
                    'topic_id':id,
                    'updatedby_id':user_id
                }
                print(FastProcedures.asset_query_add(**values), end="\n\n\n\n\n\n")
                query+=FastProcedures.asset_query_add(**values)
            print(query)
            FastProcedures.execute_query(query)
            return redirect('clients:alljobs')


class GetJobPost(generic.ListView):
    def get(self, request):
        cursor = connection.cursor()
        userId = request.session['user']['id']
        print(userId)
        cursor.execute(f'EXEC dbo.getMyJobs @user_id="{userId}"')
        joblist = dictfetchall(cursor)
        for i in joblist:
            print(i)
        return render(request, 'clients/alljobs.html', {'jobs': joblist})

class JobDetailView(generic.DetailView):
    def get(self, request, pk):
        pk = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getEachJob @id='{pk}'")
        eachjob = dictfetchall(cursor)
        return render(request, 'clients/jobdetail.html', {'jobdetail': eachjob})

class JobUpdateView(generic.UpdateView):
    # template_name = 'jobupdate.html'
    # form_class = JobPostForm
    # context_object_name = "job"

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     return JobPost.objects.filter(id= pk)

    # def get_success_url(self):
    #     return reverse("clients:alljobs")

    def get(self, request, pk):
        pk = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getEachJob @id='{pk}'")
        eachjob = dictfetchall(cursor)
        print(eachjob)
        form_class = {'form': JobUpdateForm(instance=TopicList(**eachjob[0]))}
        return render(request, 'clients/jobupdate.html', form_class)

    def post(self, request, pk):
        if request.method == 'POST':
            li = [request.session['user']['email']]
            dict = {'id':pk, 'User':request.session['user']['id']}
            for i in request.POST:
                if i != 'csrfmiddlewaretoken':
                    li.append(request.POST[i])
                    dict[i] = request.POST[i]
            print(dict)
            saved = AllProcedures.updatejob(**dict)
            return redirect('clients:alljobs')



# def jobpost(request):
#     with connection.cursor() as cursor:
#             cursor.execute(f'EXEC dbo.getCategory @city = {request.user.City}')
#             users = cursor.fetchall()
#             print(users)
#         context = {
#             'users': users,
#         }

#         if request.method == 'POST':
#             li = []
#             for i in request.POST:
#                 if i != 'csrfmiddlewaretoken':
#                     li.append(request.POST[i])
#             saved = AllProcedures.createjob(li)
#             return redirect('/client/jobpost')
#         return render(request, 'jobposting.html', context)


# class IndiJobView(generic.ListView):
#     template_name = 'construction.html'
#     context_object_name = 'myJobs'
#
#     def get_queryset(self):
#         return JobPost.objects.filter(id=self.request.GET.get('job_id'), client=self.request.user)
#
#
#
#
# class MyJobView(generic.ListView):
#     template_name = 'MyJobs.html'
#     context_object_name = 'myJobs'
#
#     def get_queryset(self):
#         return JobPost.objects.filter(client=self.request.user)
#
#
# class JobDetailView(generic.DetailView):
#     template_name = 'jobdetail.html'
#     context_object_name = 'jobdetail'
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         return JobPost.objects.filter(id= pk)
#
#
# class JobUpdateView(generic.UpdateView):
#     template_name = 'jobupdate.html'
#     form_class = JobPostForm
#     context_object_name = "job"
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         return JobPost.objects.filter(id= pk)
#
#     def get_success_url(self):
#         return reverse("clients:alljobs")
#
#
# class JobDeleteView(generic.DeleteView):
#     template_name = 'jobdelete.html'
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         return JobPost.objects.filter(id= pk)
#
#     def get_success_url(self):
#         return reverse("clients:alljobs")
