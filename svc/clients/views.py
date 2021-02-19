from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from accounts.models import UserList
from .forms import JobPostForm, JobUpdateForm, AssetsForm, ReviewForm
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
from svc.utils import AllProcedures
from django.core.paginator import Paginator
from django.core.mail import send_mail
import datetime

# # Create your views here.

def dashboard(request):
    return render(request, 'clients/dashboard.html')

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
            print(li)
            return redirect('/client/alljobs')


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
        cursor.close()
        user = eachjob[0]['User_id']
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getUserWithId @id='{user}'")
        posteduser = dictfetchall(cursor)
        return render(request, 'clients/jobdetail.html', {'jobdetail': eachjob, 'user': posteduser})

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
        pk = self.kwargs.get('pk')
        if request.method == 'POST':
            topicname = request.POST['TopicName']
            category_id = int(request.POST['Category'] or 0)
            sub_Category = int(request.POST['SubCategory'] or 0)
            isActive = request.POST.get('IsActive')
            active = AllProcedures.boolcheck(isActive)
            isClose = request.POST.get('IsClose')
            close = AllProcedures.boolcheck(isClose)
            closed_by = int(request.POST['CloseBy'] or 0)
            closereason = request.POST['ForceCloseReason']
            CLosedCategory = int(request.POST['ForceCloseCategory'] or 1)
            isNotify = request.POST.get('IsNotification')
            notify = AllProcedures.boolcheck(isNotify)
            sms = request.POST['SMSText']
            wap = request.POST['WhatsAppText']
            li = [request.user.id, request.user.City, pk, topicname, category_id, sub_Category, active, close, closed_by, closereason, CLosedCategory, notify, sms, wap]
            print(li)
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.updateJobPost @id='{pk}', @TopicName='{topicname}', @UpdatedDate='{datetime.datetime.now()}', @IsActive='{active}', @IsClose='{close}', @ForceCloseReason='{closereason}', @IsNotification='{notify}', @SMSText='{sms}', @Category_id='{category_id}', @CloseBy_id='{closed_by}', @ForceCloseCategory_id='{CLosedCategory}', @SubCategory_id='{sub_Category}', @User_id='{request.user.id}'")
            return redirect('/alljobs')

class JobDeleteView(View):
    def post(self, request, pk):
        pk = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.deleteJob @id='{pk}'")
        return redirect('/client/alljobs')


class AllProfessionals(View):
    def get(self, request):
        cursor = connection.cursor()
        if request.user.is_superuser and request.user.is_staff:
            myId = request.user.id
        else:
            myId = request.session['user']['id']
        cursor.execute(f"EXEC dbo.getProfessionalInCity @myId='{myId}'")     
        allcategories = dictfetchall(cursor)
        print(allcategories)
        paginator = Paginator(allcategories, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'clients/services.html', {'professionals': page_obj}) 


class Callback(View):
    def get(self, request, slug):
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getUser @id='{request.user.id}'")
        user = dictfetchall(cursor)
        return render(request, 'clients/callback.html', {'user': user})

    def post(self, request, slug):
        if request.method == 'POST':
            slug = self.kwargs.get('slug')
            email = request.POST['email']
            number = request.POST['number'] 
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.getEmail @username='{slug}'")
            user = dictfetchall(cursor)
            rec_email = [user[0]['email']]
            message = request.user.username + " has requested you for a callback. You may email here:" + email + ", or you may call at " + number
            send_mail(
                subject="Request for a Callback",
                message= message,
                from_email = "ouremail@gmail.com",
                recipient_list= rec_email
            )
            return render(request, 'clients/successemail.html')
 

class Review(View):
    def get(self, request, pk):
        form = ReviewForm
        id = self.kwargs.get('pk')
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getUserWithId @id='{id}'")
        user = dictfetchall(cursor)
        cursor.close()
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.myreviews @user_id='{id}'")
        allreviews = dictfetchall(cursor)
        print(allreviews)
        return render(request, 'clients/review.html', {'user': user, 'form': form, 'allreviews': allreviews})

    def post(self, request, pk):
        if request.method =='POST':
            topic = request.POST['Topic']
            review = request.POST['ReviewNote']
            touser = self.kwargs.get('pk')
            fromuser = request.user.id
            addedby = request.user.id
            IsActive = 1
            IsAdminApproved =1
            cursor = connection.cursor()
            cursor.execute(f"EXEC dbo.addreview @Topic='{topic}', @ReviewDate='{datetime.datetime.now()}', @ToUser='{touser}', @FromUser='{fromuser}', @ReviewNote='{review}', @User='{touser}', @AddedBy='{fromuser}', @AddedDate='{datetime.datetime.now()}', @IsActive='{IsActive}', @IsAdminApproved='{IsAdminApproved}'")
            return HttpResponseRedirect(self.request.path_info)





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
# def chat(request, user_id):
#     chatRoom = None
#     messages = []
#     sender = User.objects.get(id=user_id)
#     name = sender.first_name
#     if not request.user.usertype=="Professional":
#         chatRoom = ChatRecord.objects.filter(client=request.user, professional_id=user_id)
#         room_name = f'chat{user_id}{request.user.id}s'
#         client_id = request.user.id
#         professional_id = user_id
#         for i in chatRoom:
#             messages.append((i.message, i.side, name))
#     else:
#         chatRoom = ChatRecord.objects.filter(professional=request.user, client_id=user_id)
#         room_name = f'chat{request.user.id}{user_id}s'
#         professional_id = request.user.id
#         client_id = user_id
#         for i in chatRoom:
#             messages.append((i.message, not i.side, name))
#     context = {
#         'senderId': (user_id, name),
#         'room_name':room_name,
#         'messages': messages,
#         'professional_id':professional_id,
#         'client_id':client_id
#     }
#     return render(request, 'chatroom.html', context)
