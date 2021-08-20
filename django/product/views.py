from django.shortcuts import render
from product.models import Product
# Create your views here.

def products(requests):
    _products = Product.objects.all()
    return render(requests, 'product/products.html', {'products': _products})