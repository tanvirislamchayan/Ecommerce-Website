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
    product = Products.objects.get(uid=uid)
    
    if request.user.is_authenticated:
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
        size = request.GET.get('size')
        color = request.GET.get('color')
        price = request.GET.get('price')

        cart_item, created = CartItems.objects.get_or_create(
            cart = cart,
            product = product,
            item_price = price or 0,
            color_variant = ColorVariants.objects.filter(color_name = color).first() or None,
            size_variant = SizeVariants.objects.filter(size_name = size).first() or None,
        )

        redirect_url = reverse('detail', kwargs={'slug': product.slug})
        redirect_url += f'?size={size}&color={color}'

        user_name = request.user.get_full_name() if request.user.is_authenticated else "Guest"
        if created:
            messages.success(request, f'Hello, {user_name}! Your selected Product: {product.product_name}, with Size: {size}, and Color: {color} has been added to the cart successfully!')
        else:
            messages.warning(request, f'Hello, {user_name}! Your selected Product variant already exists in your cart.')

        return redirect(redirect_url)
    else:
        messages.warning(request, f'Invalid User. Please Login or Signup first')
        return redirect(reverse('login'))



def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(is_paid=False, user=request.user).first()

        if cart:
            cart_items = cart.cart_items.all()

        else:
            messages.warning(request, 'No cart items! Please add some products to cart.')
            return redirect(reverse('product'))

        if not cart_items:  # If cart_items is empty
            messages.warning(request, 'No items in the cart.')  # Display a message
            return redirect(reverse('product'))  # Redirect the user
        

        

        page = 'Cart | Django'
        context = {
            'page': page,
            'items': cart_items,
        }
        return render(request, 'account/cart.html', context=context)
    else:
        messages.warning(request, 'Please login or signup first!')
        return redirect(reverse('login'))
    



def delete(request, uid):
    cart_item = CartItems.objects.get(uid=uid)
    cart_item.delete()
    return redirect(reverse('cart'))


