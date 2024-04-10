from django.shortcuts import render
from product.models import *

def home(request):
    products = Products.objects.all().order_by('-create_at')[:3]  # Retrieve the last three products based on their creation timestamps

    page = 'Home | Django'
    context = {
        'page': page,
        'products': products
    }
    return render(request, 'home/home.html', context)



def contact(request):
    page = 'Contact Us | Django'
    context = {
        'page': page,
    }
    return render(request, 'contact/contact.html', context)


def about(request):
    page = 'About Us | Django'
    context = {
        'page': page,
    }
    return render(request, 'contact/about.html', context)



def blog(request):
    page = 'Blog | Django'
    context = {
        'page': page
    }
    return render(request, 'home/blog.html', context)



def services(request):
    page = 'Services | Django'
    context = {
        'page': page,
    }
    return render(request, 'contact/contact.html', context)

