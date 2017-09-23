from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
# Create your views here.
#User name is McGruder
#password is testpassword
def index(request):
    newUsers = User.objects.all()
    return render (request, 'first_app/index.html')
def login(request):
    login_user = User.objects.login(request.POST)
    if login_user == True:
        request.session['current_user'] = request.POST['username']
        return redirect('/travels')
    else:
        for i in login_user[1]:
            messages.error(request, i)
        return redirect("/main")

def register(request):
    register_user = User.objects.register(request.POST)
    if register_user == True:
        request.session['current_user'] = request.POST['username']
        return redirect('/travels')
    else:
        for i in register_user[1]:
            messages.error(request, i)
        return redirect("/main")

def travels(request):
    return render (request, 'first_app/test.html')
