from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('contact-us/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services')
]