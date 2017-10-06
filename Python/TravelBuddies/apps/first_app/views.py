from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .models import Trip
from django.contrib import messages
# Create your views here.
#User name is McGruder
#password is testpassword
def index(request):

    # context = {
    # 'userTrip' : Trip.objects.filter(created_by= request.session['current_user']),
    # # 'all_other_user_plans': excluded_travels,
    # 'all_users':User.objects.all(),
    # 'all_Trips': Trip.objects.exclude(created_by = request.session['current_user'])
    # }

    a = set(Trip.objects.all())
    b= set(Trip.objects.exclude(new_trips__users_id__username = request.session['current_user']))
    c = set(Trip.objects.filter(created_by = request.session['current_user']))
    excluded_travels = (a.difference(b))
    context = {
    # 'user_plans' : Trip.objects.filter(new_trips__users__username = request.session['current_user']),
    # 'user_plans' : Trip.objects.filter(created_by = request.session['current_user']),
    'user_plans' : Trip.objects.filter(created_by = request.session['current_user']),
    # 'user_plans' : User_Trip.objects.filter(trips__users__created_by = request.session['current_user']),
# user_plans' : User_Travel.objects.filter(user__email = request.session['user_name'])
    'all_users':Trip.objects.all(),
    'other_users': Trip.objects.exclude(created_by = request.session['current_user'])
    # 'new_plans': userNow
    }
    print b, "this is b"
    print a, "this is a"
    print excluded_travels, "this is travels"
    return render(request, 'first_app/index.html', context)

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

def add(request):
    return render (request, 'first_app/add.html')

def new_trip(request):
    newUser = request.session['current_user']
    new_trip = Trip.objects.new_trip(request.POST, newUser)
    if new_trip == True:
        return redirect('/main')
    else:
        for i in new_trip[1]:
            messages.error(request, i)
        return redirect('/travels/add')

def logout(request):
    return redirect ('/main')
