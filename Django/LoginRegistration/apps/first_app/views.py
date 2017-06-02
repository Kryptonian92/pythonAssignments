from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages


def index(request):
    newUsers = User.objects.all()
    print newUsers
    return render(request, 'first_app/index.html')

def login(request):
    login_user = User.objects.login(request.POST)
    if login_user == True:
        return render(request, 'first_app/success.html')
    else:
        for i in login_user[1]:
            messages.error(request, i)
        return redirect("/")

def register(request):
    register_user = User.objects.register(request.POST)
    if register_user == True:
        return render(request, 'first_app/success.html')
    else:
        for i in register_user[1]:
            messages.error(request, i)
        return redirect("/")
