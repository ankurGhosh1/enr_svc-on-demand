from django.shortcuts import render, redirect, reverse

def login_required_cus(func):
    def inner(request, **kwargs):
        if request.session.has_key('user'):
            return func(request, **kwargs)
        return redirect('accounts:login')
    return inner


def redirect_to_dash(func):
    def inner(request, **kwargs):
        if request.session.has_key('user'):
            if request.session['user']['type']=="Client":
                return redirect('clients:dashboard')
            if request.session['user']['is_staff'] and request.session['user']['is_superuser']:
                return redirect('admins:dashboard')
            return redirect('professional:dashboard')
        return func(request, **kwargs)
    return inner


def is_client(func):
    def inner(request, **kwargs):
        if request.session.has_key('user'):
            if request.session['user']['type']=="Client":
                return func(request, **kwargs)
            if request.session['user']['is_staff'] and request.session['user']['is_superuser']:
                return redirect('admins:dashboard')
            return redirect('professional:dashboard')
        return redirect('accounts:login')
    return inner


def is_professional(func):
    def inner(request, **kwargs):
        if request.session.has_key('user'):
            if request.session['user']['type']=="Client":
                return redirect('clients:dashboard')
            if request.session['user']['is_staff'] and request.session['user']['is_superuser']:
                return redirect('admins:dashboard')
            return func(request, **kwargs)
        return redirect('accounts:login')
    return inner
