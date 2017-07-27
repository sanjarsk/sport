from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)

def auth_view(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(email=email, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'invalid.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
