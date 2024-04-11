from django.urls import path
from . import views

urlpatterns = [
    path('shop/',views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/<slug>/', views.detail, name='detail')
]
