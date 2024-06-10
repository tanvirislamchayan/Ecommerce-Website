from django.shortcuts import render
from django.contrib import messages #this will show messages on html
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, logout
from .models import *
from product.models import *
from django.contrib.auth import authenticate, login as auth_login  # Renamed login function
from django.shortcuts import get_object_or_404






def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        messages.success(request, f'Hello, Your account has been varified successfully!')
        return redirect(reverse('login'))  # Assuming 'login' is the name of your login URL pattern
    except Profile.DoesNotExist:
        return HttpResponse("Invalid email Token")



"""Login"""

def login(request):

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password') 

        #Get user
        user_obj = User.objects.filter(username=email)

        #check user if not exists
        if not user_obj.exists():
            messages.warning(request, f'Invalid Username')
        
        #if user exists 
        elif user_obj.exists():
            #check if account is not varified
            if not user_obj[0].profile.is_email_verified:
                messages.warning(request, f'Hello Mr./Mst. {user_obj[0].first_name}. Your account is not varified. Please check your email and varify Your account.')
                return HttpResponseRedirect(request.path_info) 
            
            #if account is varified
            elif user_obj[0].profile.is_email_verified:
                #check if user authenticated (password)
                user_auth = authenticate(username=email, password=password)
                #if true
                if user_auth is not None:
                    auth_login(request, user_auth)
                    return redirect(reverse('home'))

                #if False
                else:
                    messages.warning(request, f'Invalid Password')
                    return HttpResponseRedirect(request.path_info)
            


    page = 'Login | Django'
    context = {
        'page': page
    }
    return render(request, 'account/login.html', context)



"""sign-up"""

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #check if user already exists or not
        user_obj = User.objects.filter(username = email)
        if user_obj.exists():
            messages.warning(request, "The username or email already exists! Please go and login.")
            return HttpResponseRedirect(request.path_info)
        
        #if user doesnot exist creaet new user
        elif not user_obj.exists():
            user_obj = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = email
            ) #user created successfuly
            user_obj.set_password(password) #set Hash password for user and save
            user_obj.save()
            messages.success(request, f'Hi! Mr/Mst. {first_name}. \n'
                             f'we have sent a mail on your emial " {email} ". \n'
                             f'Please check and verify your account.')
            return redirect(reverse('login'))


    page = 'Sign UP | Django'
    context = {
        'page': page
    }
    return render(request, 'account/login.html', context=context)



def profile(request):
    page = 'Profile | Django'
    context = {
        'page': page,
    }
    return render(request, "account/profile.html", context)



def logout_user(request):
    logout(request)
    return redirect(reverse('home'))


def add_cart(request, uid):
    product = get_object_or_404(Products, uid=uid)

    if request.user.is_authenticated:
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

        size = request.GET.get('size')
        color = request.GET.get('color')
        price = float(request.GET.get('price', 0))  # Convert price to float
        quantity = 1
        total_price = price * quantity

        color_variant = ColorVariants.objects.filter(color_name=color).first()
        size_variant = SizeVariants.objects.filter(size_name=size).first()

        cart_item, created = CartItems.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={
                'item_price': price,
                'color_variant': color_variant,
                'size_variant': size_variant,
                'quantity': quantity,
                'total_price': total_price
            }
        )

        if not created:
            # If the item already exists in the cart, update the quantity and total price
            cart_item.quantity += quantity
            cart_item.total_price += total_price
            cart_item.save()

        user_name = request.user.get_full_name()
        if created:
            messages.success(request,
                             f'Hello, {user_name}! Your selected Product: {product.product_name}, with Size: {size}, and Color: {color} has been added to the cart successfully!')
        else:
            messages.warning(request,
                             f'Hello, {user_name}! Your selected Product variant already exists in your cart. Quantity updated.')

        redirect_url = reverse('detail', kwargs={'slug': product.slug}) + f'?size={size}&color={color}'
        return redirect(redirect_url)
    else:
        messages.warning(request, 'Invalid User. Please Login or Signup first')
        return redirect(reverse('login'))


def cart(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login or signup first!')
        return redirect(reverse('login'))

    cart = Cart.objects.filter(is_paid=False, user=request.user).first()
    if not cart:
        messages.warning(request, 'No cart items! Please add some products to the cart.')
        return redirect(reverse('product'))

    cart_items = cart.cart_items.all()

    if not cart_items.exists():
        messages.warning(request, 'No cart items! Please add some products to the cart.')
        return redirect(reverse('product'))


    page = 'Cart | Django'
    context = {
        'page': page,
        'items': cart_items,
        'cart': cart
    }
    return render(request, 'account/cart.html', context=context)



def delete(request, uid):
    cart_item = CartItems.objects.get(uid=uid)
    cart_item.delete()
    return redirect(reverse('cart'))


#*Update cart
def updateCart(request, uid):
    delta_qty = int(request.GET.get('delta', 0))

    cart_item = get_object_or_404(CartItems, uid=uid)
    qty = cart_item.quantity
    print(f'Current quantity: {qty}')
    item_price = cart_item.item_price

    # Update quantity
    if qty + delta_qty <= 1:
        qty = 1
    else:
        qty += delta_qty

    print(f'Updated quantity: {qty}')

    # Update the cart item
    cart_item.quantity = qty
    cart_item.save()  # This will automatically update the total_price and the cart subtotal

    return redirect(reverse('cart'))


def applyCoupon(request):
    coupon_code = request.GET.get('coupon', '').strip()

    if not coupon_code:
        messages.warning(request, 'No coupon code provided!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    coupon_obj = Coupon.objects.filter(coupon_code__icontains=coupon_code).first()
    if not coupon_obj:
        messages.warning(request, 'Invalid Coupon! Please try again.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    cart = Cart.objects.filter(is_paid=False, user=request.user).first()
    if not cart:
        messages.warning(request, 'No active cart found!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    if cart.coupon:
        messages.warning(request, 'Coupon already used!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    if cart.subTotal < coupon_obj.minimum_amount:
        messages.warning(request, f'Total amount must be greater than {coupon_obj.minimum_amount}!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    cart.subTotal -= coupon_obj.discount_price
    cart.save()
    messages.success(request, 'Coupon applied successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
