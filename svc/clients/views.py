from django.shortcuts import render, redirect, reverse
from django.views import generic
# from .models import User, JobPost, ChatRecord
from .forms import CustomClientUserForm #, JobPostForm
from django.views.generic import View

# Create your views here.

class SignupView(generic.CreateView):
    template_name = 'signup.html'
    form_class = CustomClientUserForm

    def get_success_url(self):
        return reverse('clients:jobpost')

    def form_valid(self, form):
        if form.is_valid():
            client = form.save(commit=False)
            client.set_password(form.cleaned_data["password"])
            client.save()
            print(client)
            return super(SignupView, self).form_valid(form)


class HomeView(View):
    template_name = 'home.html'
    def get(self, request):
        # users = User.objects.all().exclude(id=request.user.id).exclude(is_staff=True)  # conditions need to be set as we develop
        context = {'users':"Asdf"}
        # print(users)
        return render(request, self.template_name, context)

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
