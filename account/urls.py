from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('sign-up/', views.signup, name='signup'),
    path('activate/<email_token>/',views.activate_email, name='activate_email'),
    path('profile/', views.profile, name='profile'),
    path('log-out/', views.logout_user, name='logout')
]