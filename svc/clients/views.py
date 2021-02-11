
from django.shortcuts import *
from svc.utils import AllProcedures
# from django.views import generic
# from .models import User, JobPost, ChatRecord, Category, SubCategory
# from .forms import CustomClientUserForm, JobPostForm
# from django.views.generic import View
# from django.db import connection
#
#
# # Create your views here.


def profile(request):
    user = AllProcedures.getUserWithId(request.session['user']['id'])
    print(user[0].first_name)
    return render(request,'clients/profile.html',{'profile':user})
#
#
#
#
# class SignupView(generic.CreateView):
#     template_name = 'signup.html'
#     form_class = CustomClientUserForm
#
#     def get_success_url(self):
#         return reverse('clients:jobpost')
#
#     def form_valid(self, form):
#         if form.is_valid():
#             client = form.save(commit=False)
#             client.set_password(form.cleaned_data["password"])
#             client.save()
#             print(client)
#             return super(SignupView, self).form_valid(form)
#
#
# class HomeView(View):
#     template_name = 'home.html'
#     def get(self, request):
#         users =[]
#         if request.user.is_authenticated:
#             if request.user.usertype=="Professional":
#                 Customer = "Customer"
#                 with connection.cursor() as cursor:
#                     cursor.execute(f'EXEC dbo.allUserTypeExceptMe @userId = {request.user.id}, @userType = "{Customer}"')
#                     users = cursor.fetchall()
#             else:
#                 Professional = "Professional"
#                 with connection.cursor() as cursor:
#                     cursor.execute(f'EXEC dbo.allUserTypeExceptMe @userId = {request.user.id}, @userType = "{Professional}"')
#                     users = cursor.fetchall()
#         context = {'users': users}
#         # print(users)
#         return render(request, self.template_name, context)
#
# class JobPostingView(generic.CreateView):
#     template_name = 'jobpost.html'
#     form_class = JobPostForm

#     def get_success_url(self):
#         return reverse('clients:alljobs')

#     def form_valid(self, form):
#         if form.is_valid():
#             job = form.save(commit=False)
#             job.client = self.request.user
#             job.save()
#             print(job)
#             return super(JobPostingView, self).form_valid(form)
#
#
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