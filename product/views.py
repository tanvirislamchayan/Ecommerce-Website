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