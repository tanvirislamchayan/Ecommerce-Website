
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('sign-up/', views.signup, name='signup'),
    path('activate/<email_token>/', views.activate_email, name='activate_email'),
    path('profile/', views.profile, name='profile'),
    path('log-out/', views.logout_user, name='logout'),
    path('show-cart/', views.cart, name='cart'),
    path('add-cart/<uuid:uid>', views.add_cart, name='add_cart'),
    path('delete-cart-itrm/<uuid:uid>/', views.delete, name='delete'),
    path('update-cart/<uuid:uid>', views.updateCart, name='updateCart'),  # Updated pattern
    path('update-cart/apply-coupon', views.applyCoupon, name='applyCoupon'),  # Updated pattern
]
