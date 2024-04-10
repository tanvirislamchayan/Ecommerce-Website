from django.shortcuts import render
from .models import *


def product(request):
    products = Products.objects.all().order_by('-create_at')


    page = 'Shop | Django e-Com'
    context = {
        'page': page,
        'products':products
    }
    return render(request, 'product/product.html', context=context)



def cart(request):
    page = 'Cart | Django e-Com'
    context = {
        'page': page,
    }
    return render(request, 'product/cart.html', context=context)



def checkout(request):
    page = 'Checkout | Django'
    context = {
        'page': page
    }
    return render(request, 'product/checkout.html', context)


def detail(request, slug):
    try:
        product = Products.objects.get(slug=slug)
        page = 'Detail | Django'
        context = {
            'page': page,
            'product':product
        }
        return render(request, 'product/detail.html', context=context)
    except Exception as e:
        print(e)