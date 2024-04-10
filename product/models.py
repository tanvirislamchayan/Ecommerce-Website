from django.db import models
from base.models import BaseModel #Imported the base model just created on base app it 
from django.utils.text import slugify #It will be used to generate slug



# Create your models here.


"""This is first class or model of a django website
Every product has a category so we must declear a category for that product"""

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='Categories')
    slug = models.SlugField(unique=True, null=True, blank=True) #slug will help to get linking like this "Poduct Image => product-image"


    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.category_name




"""Another class product where we will save products and it must pass category on this"""
class Products(BaseModel):


    product_name = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_price = models.IntegerField()
    product_description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Products, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.product_name






"""This models is for images. we are not gonna upload one image for one product we are gonna upload multiple images on 
one products so we need a new model for images"""
class ProductImage(BaseModel):


    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_images')
    images = models.ImageField(upload_to='Products')

