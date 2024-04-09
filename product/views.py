from django.shortcuts import render

# Create your views here.



def product(request):
    page = 'Shop | Django e-Com'
    context = {
        'page': page,
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


def detail(request):
    page = 'Detail | Django'
    context = {
        'page': page
    }
    return render(request, 'product/detail.html', context=context)