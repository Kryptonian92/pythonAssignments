from django.shortcuts import render
from . models import Users

# Create your views here.
def index(request):
    print "*"*50
    new = Users.objects.all()
    print (new)
    return render(request, 'first_app/index.html')
