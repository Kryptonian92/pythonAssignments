from django.shortcuts import render, HttpResponse, redirect
from .models import Trip, User_Trip, User
from django.contrib import messages

def success(request):

    # context = {
    # 'userTrip' : Trip.objects.filter(created_by= request.session['current_user']),
    # # 'all_other_user_plans': excluded_travels,
    # 'all_users':User.objects.all(),
    # 'all_Trips': Trip.objects.exclude(created_by = request.session['current_user'])
    # }

    a = set(Trip.objects.all())
    b= set(Trip.objects.filter(new_trips__users__username = request.session['current_user']))
    excluded_travels = (a.difference(b))
    context = {
    # 'user_plans' : Trip.objects.filter(new_trips__users__username = request.session['current_user']),
    'user_plans' : Trip.objects.filter(created_by = request.session['current_user']),
    'all_other_user_plans': excluded_travels,
    'all_users':Trip.objects.all(),
    'userTrips': User_Trip.objects.all()
    }
    print b, "this is b"
    print a, "this is a"
    print excluded_travels, "this is travels"
    return render(request, 'main_app/index.html', context)

def add (request):
    return render(request, 'main_app/add.html')
def new_trip(request):
    newUser = request.session['current_user']
    new_trip = Trip.objects.new_trip(request.POST, newUser)
    if new_trip == True:
        return redirect('/success')
    else:
        for i in new_trip[1]:
            messages.error(request, i)
        return redirect('/main/add')

def trip_info(request, id):
    context = {
    'trips': Trip.objects.filter(id = id )
    }
    return render(request, 'main_app/destination.html', context)

def join(request, id):
    t1 = Trip.objects.filter(id = id)
    u1 = User.objects.filter(username = request.session['current_user'])

    trip_join = User_Trip.objects.create(users=u1[0], trips=t1[0])
    print trip_join
    return redirect ('/success')
