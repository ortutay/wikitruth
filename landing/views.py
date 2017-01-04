from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from landing.forms import SignupForm, SigninForm


def index(request):
    return render(request, 'landing/index.html')


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        context = { 'form': form }
        return render(request, 'landing/signup.html', context)

    def post(self, request):
        form = SignupForm(request.POST)
        if not form.is_valid():
            return render(request, 'landing/signup.html', {'form': form})
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'])
        login(request, user)
        return redirect('index')


class SigninView(View):
    def get(self, request):
        form = SigninForm()
        context = { 'form': form }
        return render(request, 'landing/signin.html', context)

    def post(self, request):
        form = SigninForm(request.POST)
        if not form.is_valid():
            return render(request, 'landing/signin.html', {'form': form})
        form.login(request)
        return redirect('index')


def signin(request):
    if not request.method == 'POST':
        return redirect('index')

    form = SignupForm(request.POST)


def signout(request):
    logout(request)
    return redirect('index')

