from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
import random
# Create your views here.
from django.shortcuts import render
from django.db import connection


def customerhomepage(request):
    # Retrieve random products from the database
    products = Product.objects.all()
    random_products = random.sample(list(products), min(len(products), 24))  # Get 3 random products

    return render(request, 'customer/customerhomepage.html', {'random_products': random_products})


def categories(request):
    return render(request,'customer/categories.html')


def homeaccessories(request):
    home = Product.objects.filter(id__range=(25, 32))
    return render(request, 'customer/homeaccesories.html' , {'home': home})


# views.py
def mobiles(request):
    # Retrieve products with IDs ranging from 1 to 22 and sort them by price
    mobile = Product.objects.filter(id__range=(1, 24))

    return render(request, 'customer/mobiles.html', {'mobile': mobile})

def shirts(request):
    shirt = Product.objects.filter(id__range=(33, 40))

    return render(request, 'customer/shirts.html', {'shirt': shirt})


def contact(request):
    if request.method == 'POST':
        return HttpResponse("<h1>Succesfully sent</h1>")
    return render(request,'customer/contact.html')


def search_product(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Filter products by name containing the query
        results = Product.objects.filter(name__icontains=query)
        # Sort the filtered results by price in ascending order
        results = results.order_by('price')

    return render(request, 'customer/search_product.html', {'results': results})