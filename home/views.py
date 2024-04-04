from django.shortcuts import render

# Create your views here.

def home(request):
    page = 'Home | Django-Ecomm'
    context = {
        'page': page,
    }
    return render(request, 'home/home.html', context)


def contact(request):
    page = 'Contact Us | Django-Ecomm'
    context = {
        'page': page,
    }
    return render(request, 'contact/contact.html', context)


def about(request):
    page = 'About Us | Django-Ecomm'
    context = {
        'page': page,
    }
    return render(request, 'contact/about.html', context)