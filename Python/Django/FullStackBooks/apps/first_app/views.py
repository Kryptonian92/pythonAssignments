
from django.shortcuts import render, HttpResponse, redirect
from .models import Books

def index(request):
    books = Books.objects.all()
    context = {"books": books}
    return render(request, 'first_app/index.html', context)

def add_book(request):
    Books.objects.create(title = request.POST['title'], author = request.POST['author'], category = request.POST['category'])
    books = Books.objects.all()
    print books
    return redirect('/')

# def remove_book(request):
