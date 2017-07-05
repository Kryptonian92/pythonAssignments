from django.shortcuts import render, HttpResponse
import random
from datetime import datetime

def index(request):
    context = {
    "somekey": datetime.now()
    }
    return render(request, 'first_app/index.html', context)
