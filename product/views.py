from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def product(request):
    products = Products.objects.all().order_by('-create_at')
    menual_dis = []

    for product in products:
        menual_dis.append(product.product_manual_discount)

    page = 'Shop | Django e-Com'
    context = {
        'page': page,
        'products':products
    }
    return render(request, 'product/product.html', context=context)







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
        updated_price = None
        size = None
        color = None

        # Get price based on size
        if 'size' in request.GET:
            size = request.GET.get('size')
            if not product.product_manual_discount:
                size_var = SizeVariants.objects.get(size_name=size)
                
                if size_var.discount and size_var.discount > 0:
                    discount_price = (product.product_price * size_var.discount) / 100
                    updated_price = product.product_price - discount_price

                if size_var.manual_discount and size_var.manual_discount > 0:
                    updated_price = product.product_price - size_var.manual_discount

        # Get price based on color
        if 'color' in request.GET:
            color = request.GET.get('color')
            if not product.product_manual_discount and not product.product_manual_discount>0:
                try:
                    color_var = ColorVariants.objects.get(color_name=color)
                    print(color_var)
                    
                    if color_var.discount and color_var.discount > 0:
                        discount_price = (product.product_price * color_var.discount) / 100
                        updated_price = product.product_price - discount_price

                    if color_var.manual_discount and color_var.manual_discount > 0:
                        updated_price = product.product_price - color_var.manual_discount
                except ColorVariants.DoesNotExist:
                    pass  # If color variant doesn't exist, continue without updating updated_price
            
        context = {
            'page': page,
            'product': product,
            'updated_price': updated_price,
            'selected_size': size,
            'selected_color': color
        }

        return render(request, 'product/detail.html', context)
    except Exception as e:
        print(e)
        return HttpResponse("An error occurred.")

