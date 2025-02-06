from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  # Bosh sahifaga qaytish
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Muvaffaqiyatli login bo'lgandan keyin bosh sahifaga o'tadi
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def base_view(request):
    return render(request, 'index.html')
