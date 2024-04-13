from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from base.emails import send_email_activation_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from product.models import *
import uuid


# Create your models here.

"""User Class"""
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='Profiles')

    def get_cart_counter(self):
        return CartItems.objects.filter(cart__is_paid=False, cart__user=self.user).count()
    
@receiver(post_save, sender=User)
def send_email_verification(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance, email_token = email_token)
            email = instance.email
            send_email_activation_mail(email, email_token)

    except Exception as e:
        print(e)


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    is_paid = models.BooleanField(default=False)


class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    color_variant = models.ForeignKey(ColorVariants,on_delete=models.SET_NULL, null=True, blank=True)
    size_variant = models.ForeignKey(SizeVariants, on_delete=models.SET_NULL,null=True, blank=True)
    item_price = models.IntegerField(default=0, null=True, blank=True)
