from django.shortcuts import render, HttpResponse, redirect
from .models import Users

def index(request):
    return render(request, 'first_app/index.html')

def process(request):
    result = Users.objects.register(request.POST['email'])
    if result == True:
        return redirect('/success')
    elif 'error' in result:
        request.session['error'] = result['error']
        return redirect('/')


def success(request):
    context = {
        'result': Users.objects.all()
    }
    last = len(context['result']) - 1
    context['current'] = context['result'][last]
    request.session.clear()
    return render(request, 'first_app/success.html', context)
