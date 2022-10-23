from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from main.forms import CustomUserCreationForm


def index(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        messages.success(request, ("* Неверный логин или пароль"))
        return redirect('index')
    return render(request, 'main/index.html')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def main(request):
    return render(request, 'main/main.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def auth(request):
    return HttpResponse("<h1>You're logged in</h1>")
