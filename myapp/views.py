from django.shortcuts import render
from .models import Product

# Create your views here.

def product_index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

def product_show(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'myapp/show.html', {'product': product})