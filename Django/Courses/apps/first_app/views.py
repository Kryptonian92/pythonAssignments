
from django.shortcuts import render, HttpResponse, redirect
from .models import Courses

def index(request):
    context = {
        "courses": Courses.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def add_course(request):
    Courses.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def remove(request, id):
    context = {
        'courses': Courses.objects.get(id = id)
    }
    return render(request, 'first_app/remove.html', context)

def delete(request, id):
    Courses.objects.filter( id = id).delete()
    return redirect("/")
