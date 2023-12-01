from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    products = Product.objects.all()
    context= {'products': products}
    return render(request,'wed/home.html', context)
def cart(requset):
    context= {}
    return render(requset, 'wed/cart.html', context)
def checkout(requset):
    context= {}
    return render(requset, 'wed/checkout.html', context)