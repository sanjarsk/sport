from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import  EditProfileForm
from accounts.models import User
from django.db import transaction
from django.contrib.auth import update_session_auth_hash





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

def profile(request):
    profile = User.objects.get(pk=request.user.pk)
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,('Your profile was successfully updated!'))
            return redirect('/accounts/profile/')
        else:
            messages.error(request, ('Please enter the correctly '))
    else:
        user_form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'user_form': user_form })
