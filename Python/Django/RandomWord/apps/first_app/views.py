from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

    randword = {'word': get_random_string(length=14)}

    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    print (request.session['count'])
    return render(request, 'first_app/index.html', randword)

def process(request):

    return redirect('/')

def clearses(request):

    request.session.clear()
    return redirect('/')
