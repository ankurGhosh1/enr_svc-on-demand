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


def getSubCats(request):
    if request.method=='POST':
        print(request)
        cat_id = request.POST['cat_id']
        cursor = connection.cursor()
        subCategory = cursor.execute(f"SELECT * FROM testenr.dbo.accounts_subcategorylist WHERE Category_id='{cat_id}'")
        subCategory =  dictfetchall(subCategory)
        print(subCategory)
        return JsonResponse(subCategory, safe=False)

def getCats(request):
    if request.method=='POST':
        print(request)
        city_id = request.POST['city_id']
        cursor = connection.cursor()
        subCategory = cursor.execute(f"SELECT * FROM testenr.dbo.accounts_categorylist WHERE id IN (SELECT [category_id] FROM testenr.dbo.accounts_categoryincity WHERE city_id='{city_id}')")
        subCategory =  dictfetchall(subCategory)
        print(subCategory)
        return JsonResponse(subCategory, safe=False)


class JobPostView(generic.CreateView):
    assetForm = inlineformset_factory(TopicList, AssetsDetailList, AssetsForm, extra=1)
    def get(self, request):
        cursor = connection.cursor()
        city = cursor.execute("SELECT * FROM testenr.dbo.accounts_citylist")
        city =  dictfetchall(city)
        category = cursor.execute("SELECT * FROM testenr.dbo.accounts_categorylist")
        category =  dictfetchall(category)
        subCategory = cursor.execute("SELECT * FROM testenr.dbo.accounts_subcategorylist")
        subCategory =  dictfetchall(subCategory)
        form_class = {'form': JobPostForm, 'cat':category, 'city':city, 'subCat':subCategory, 'assetsform': self.assetForm}
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
            kwargs = {}
            for i in request.POST:
                if i !="csrfmiddlewaretoken":
                    kwargs[i] = request.POST[i]
            _, id = AllProcedures.createjob(**kwargs, User=user_id)
            for i in request.POST:
                print(i)
                if 'SubCategory-' in i:
                    query+=FastProcedures.subcat_query_add(topic_id=id, subcat_id=request.POST[i])
            if query:
                FastProcedures.execute_query(query)
            query = ''
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
            if query:
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
        print(eachjob)
        id = eachjob[0]['User_id']
        cursor = connection.cursor()
        cursor.execute(f"EXEC dbo.getUserWithId @id='{id}'")
        user = dictfetchall(cursor)
        print(user)
        return render(request, 'clients/jobdetail.html', {'jobdetail': eachjob, 'user': user})

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
        cursor.execute(f"EXEC dbo.getMyCityJobs @user_Id='{myId}'")
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






def MyProfile(request):
    return render(request, 'clients/myprofile.html')


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
