from django.db import models
from base.models import BaseModel #Imported the base model just created on base app it 



# Create your models here.


"""This is first class or model of a django website
Every product has a category so we must declear a category for that product"""

class Category(BaseModel):


    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='Categories')




"""Another class product where we will save products and it must pass category on this"""
class Products(BaseModel):


    product_name = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_price = models.IntegerField()
    product_description = models.TextField()






"""This models is for images. we are not gonna upload one image for one product we are gonna upload multiple images on 
one products so we need a new model for images"""
class ProductImage(BaseModel):


    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_images')
    images = models.ImageField(upload_to='Products')

