from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    print "*"*50
    if 'current_gold' not in request.session:
        request.session['current_gold'] = 0
        request.session['log'] = []
    else:
        pass
    return render(request, 'first_app/index.html')

def process(request):
    if request.POST['building']=='farm':
        Gold = random.randrange(10,21)
        request.session['current_gold'] += Gold
        request.session['log'].insert(0, ("You have earned {} gold from the farm!{}").format(Gold, datetime.utcnow()))
    if request.POST['building']=='cave':
        Gold = random.randrange(5,11)
        request.session['current_gold'] += Gold
        request.session['log'].insert(0, ("You have earned {} gold from the farm!{}").format(Gold, datetime.utcnow()))
    if request.POST['building']=='house':
        Gold = random.randrange(2,6)
        request.session['current_gold'] += Gold
        request.session['log'].insert(0, ("You have earned {} gold from the farm!{}").format(Gold, datetime.utcnow()))
    if request.POST['building']=='casino':
        Gold = random.randrange(-50,51)
        request.session['current_gold'] += Gold
        if Gold < 0:
            request.session['log'].insert(0, ("loss" " " "you lost {} gold {}").format(Gold, datetime.utcnow()))
        else:
            request.session['log'].insert(0, ("earn" " " "you earned {} gold {}").format(Gold, datetime.utcnow()))
    return redirect ("/")


def reset(request):
    request.session.clear()
    return redirect ("/")
