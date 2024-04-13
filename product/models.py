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



""" Color variants """
class ColorVariants(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0, null=True, blank=True)
    discount = models.IntegerField(default=0, null=True, blank=True)
    manual_discount = models.IntegerField(null=True, blank=True, default=0)



    def __str__(self) -> str:
        return f'{self.color_name}'


class SizeVariants(BaseModel):
    price = models.IntegerField(default=0, null=True, blank=True)
    discount = models.IntegerField(default=0, null=True, blank=True)
    size_name = models.CharField(max_length=20)
    manual_discount = models.IntegerField(null=True, blank=True, default=0)


    def __str__(self) -> str:
        return f'{self.size_name}'
    



"""Another class product where we will save products and it must pass category on this"""
class Products(BaseModel):


    product_name = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_price = models.IntegerField()
    product_description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    color_variant = models.ManyToManyField(ColorVariants, blank=True)
    size_variant = models.ManyToManyField(SizeVariants, blank=True)
    product_manual_discount = models.IntegerField(default=0, blank=True, null=True)
    discount_price = models.IntegerField(null=True, blank=True)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        if self.product_manual_discount and self.product_manual_discount > 0:
            self.discount_price = self.product_price - self.product_manual_discount
        super(Products, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.product_name


    # def get_updated_price(self, size):
    #     size_var = SizeVariants.objects.get(size_name=size)
    #     if size.discount:
    #         discount = (self.product_price * size_var.discount) / 100
    #         updated_price = round((self.product_price - discount), 2)
    #     if size.price:
    #         additional_price = (self.product_price * size_var.price) / 100
    #         updated_price = round((self.product_price  additional_price), 2)
    #     return updated_price




"""This models is for images. we are not gonna upload one image for one product we are gonna upload multiple images on 
one products so we need a new model for images"""
class ProductImage(BaseModel):


    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_images')
    images = models.ImageField(upload_to='Products')

