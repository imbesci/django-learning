from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme as urlcheck

# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User has been successfully created')
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', context={'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
        if request.POST.get('auth_failed'):
            return redirect(request.POST.get('auth_failed'))
        else:
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', context={'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('articles:list')
