from django.shortcuts import render, redirect, reverse
from django.views import generic

from .models import User, JobPost
from .forms import CustomClientUserForm, JobPostForm

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


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class JobPostingView(generic.CreateView):
    template_name = 'jobposting.html'
    form_class = JobPostForm

    def get_success_url(self):
        return reverse('clients:alljobs')

    def form_valid(self, form):
        if form.is_valid():
            job = form.save(commit=False)
            job.client = self.request.user
            job.save()
            print(job)
            return super(JobPostingView, self).form_valid(form)


class AllJobView(generic.ListView):
    template_name = 'alljobs.html'
    context_object_name = 'alljobs'

    def get_queryset(self):
        return JobPost.objects.all()


class JobDetailView(generic.DetailView):
    template_name = 'jobdetail.html'
    context_object_name = 'jobdetail'

    def get_queryset(self):
        return JobPost.objects.filter(client=self.request.user)