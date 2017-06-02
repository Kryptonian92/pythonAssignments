from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages


def index(request):
    newUsers = User.objects.all()
    # request.session.flush()
    # User.objects.all().delete()
    return render(request, 'login_app/index.html')

def login(request):
    login_user = User.objects.login(request.POST)
    if login_user == True:
        request.session['current_user'] = request.POST['username']
        return redirect('main/success')
    else:
        for i in login_user[1]:
            messages.error(request, i)
        return redirect("/")

def register(request):
    register_user = User.objects.register(request.POST)
    if register_user == True:
        request.session['current_user'] = request.POST['username']
        return redirect('main/success')
    else:
        for i in register_user[1]:
            messages.error(request, i)
        return redirect("/")

def success(request):
    return redirect('main/success')
