from django.shortcuts import render
from django.http import HttpResponse




def dashboard(request):
    return render(request, 'professional/dashboard.html')


def MyProfile(request):
    return render(request, 'professional/myprofile.html')
