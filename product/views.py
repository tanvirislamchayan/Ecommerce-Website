from django.shortcuts import render

# Create your views here.

def home(request):
    page = 'Home'
    context = {
        'page': page,
    }
    return render(request, 'home/home.html', context=context)


def product(request):
    page = 'Shop'
    context = {
        'page': page,
    }
    return render(request, 'product/product.html', context=context)
