from django.shortcuts import render, redirect, reverse
from django.views import generic
from accounts.models import UserList
from .forms import JobPostForm, JobUpdateForm
from django.views.generic import View
from django.db import connection
from svc.utils import AllProcedures


# # Create your views here.
def dashboard(request):
    return render(request, 'clients/dashboard.html')

def chat(request, user_id):
    chatRoom = None
    messages = []
    if request.session.has_key('user'):
        user = AllProcedures.getUserWithId(user_id)
        name = user[5]
        my_id = request.session['user']['id']
        if not request.session['user']['type']=="Professional":
            messages = AllProcedures.getChatRecord(client_id=my_id, professional_id=user_id)
            room_name = f'chat{user_id}{my_id}s'
            professional_id = user_id
            client_id = my_id
            messages = [(i[0], i[1], name) for i in messages]
        else:
            messages = AllProcedures.getChatRecord(client_id=user_id, professional_id=my_id)
            room_name = f'chat{my_id}{user_id}s'
            professional_id = my_id
            client_id = user_id
            messages = [(i[0], not i[1], name) for i in messages]
        context = {
            'senderId': (user_id, name),
            'room_name':room_name,
            'messages': messages,
            'professional_id':professional_id,
            'client_id':client_id
        }
        return render(request, 'chatroom.html', context)
    return redirect('accounts:login')


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class JobPostView(generic.CreateView):
    def get(self, request):
        form_class = {'form': JobPostForm}
        return render(request, 'clients/jobposting.html', form_class)

    def post(self, request):
        if request.method == 'POST':
            li = []
            for i in request.POST:
                if i != 'csrfmiddlewaretoken':
                    li.append(request.POST[i])
            saved = AllProcedures.createjob(li)
            return redirect('/alljobs')


class GetJobPost(generic.ListView):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(f'EXEC dbo.getAllJobs')
        joblist = dictfetchall(cursor)
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
        form_class = {'form': JobUpdateForm}
        pk = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getEachJob @id='{pk}'")
        eachjob = dictfetchall(cursor)
        return render(request, 'clients/jobupdate.html', form_class)

    def post(self, request, pk):
        if request.method == 'POST':
            li = [request.user.email, request.user.City]
            for i in request.POST:
                if i != 'csrfmiddlewaretoken':
                    li.append(request.POST[i])
            saved = AllProcedures.createjob(li)
            return redirect('/alljobs')



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
#
#
#
