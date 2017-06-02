from django.shortcuts import render, HttpResponse
from .models import Product


def index(request):
    Product.objects.create(name = "Laptop", description = "2015 Macbook Pro retiena Display", weight = "25", price = "50", cost = "20", category = "Electronics")
    Product.objects.create(name = "M3", description = "Turbo charged BMW", weight = "2500", price = "5000.00", cost = "9000", category = "Car")
    Product.objects.create(name = "iMac", description = "2015 iMac retiena Display", weight = "25", price = "50", cost = "20", category = "Electronics")
    product = Product.objects.all()
    print (product)
    return render(request, 'first_app/index.html')

# Create your views here.
