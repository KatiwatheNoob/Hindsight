from django.db import models
import datetime 
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import os



#Categories
class Category(models.Model):
    name = models.CharField(max_length=50)  

    def __str__(self):
        return self.name
    #Fix Spelling
    class Meta:
      verbose_name_plural = 'categories'
    

#Parcel Properties
class Parcel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    size_of_land = models.FloatField()
    land_unit = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    address = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/parcels/')
    
    def __str__(self):
        return self.name
    


   
    
#Services
class Service(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/services/',default='uploads/default-service-image.png')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    def __str__(self):
     
        return self.name









class MainService(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/services/', default='uploads/default-mainservice-image.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name








#SubscribedEmails
class SubscribedEmail(models.Model):
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
    





# Categories


class Property(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    size_of_land = models.FloatField()
    land_unit = models.CharField(max_length=10)
    subdivision = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=None)
    description = models.TextField(blank=True, null=True)
    structures = models.IntegerField(blank=True, null=True)
    main_image = models.ForeignKey('Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='main_property')
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    google_maps_url = models.URLField(blank=True, null=True,max_length=500)
    


    @property
    def formatted_price(self):
        # Format the price with commas
        return "{:,}".format(self.price)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Properties'

class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images',default=1)
    image = models.ImageField(upload_to='property_images/')
    is_main_image = models.BooleanField(default=False)

    def __str__(self):
        return self.image.name



    
    


