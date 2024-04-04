from django.urls import path
from . import views

urlpatterns = [
    path('shop/',views.product, name='product'),
    path('show-cart/', views.cart, name='cart')
]
