from django.shortcuts import render, HttpResponse, redirect
from .models import Team, User_Team
from django.contrib import messages

def success(request):
    context = {
        "teams": Team.objects.all(),
        "your_team" Teams.objects.filter(),
    }
    return render(request, 'team_app/success.html', context)

def create_team(request):
    create_team = Team.objects.create_team(request.POST)
    if create_team == True:
        return redirect('/success')
    else:
        pass

def remove(request, id):
    context = {
        'teams' : Team.objects.get(id = id)
    }
    return render(request, 'team_app/remove.html', context)

def delete(request, id):
    Team.objects.filter(id = id).delete()
    return redirect('/success')

# def current_team(request, id):
#     context = {
#         'current_team': Teams.objects.get(id = id)
#     }
#     return render(request, 'team_app/teams.html')

# def login(request):
#     login_user = User.objects.login(request.POST)
#     if login_user == True:
#         return render(request, 'login_app/success.html')
#     else:
#         for i in login_user[1]:
#             messages.error(request, i)
#         return redirect("/")
#
# def register(request):
#     register_user = User.objects.register(request.POST)
#     if register_user == True:
#         return render(request, 'login_app/success.html')
#     else:
#         for i in register_user[1]:
#             messages.error(request, i)
#         return redirect("/")
