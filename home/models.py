from django.db import models
from .models import *

# Create your models hereeee.
class mypost(models.Model):
    user = models.TextField(null=True)
    title = models.TextField(max_length=1000)
    type = models.TextField()
    object = models.TextField()
    descrip = models.TextField(max_length=10000000)
    address = models.TextField()     #country
    city = models.TextField(null=True)
    district = models.TextField(null=True)
    name = models.TextField(max_length=1000)
    pnum = models.IntegerField(null=True, blank=True)
    email = models.TextField(max_length=1000)
    images = models.ImageField(null=True ,blank=True , upload_to='images/')


    def _str_(self):
        return self.name


class comment(models.Model):
    
    postid = models.IntegerField(null=True, blank=True)
    user = models.TextField(null=True)
    mail = models.TextField(null=True)
    message = models.TextField(null=True)
    


    def _str_(self):
        return self.name


class blog(models.Model):
    

    title = models.TextField(null=True)
    image = models.TextField(null=True)
    descrip_short = models.TextField(null=True)
    descrip = models.TextField(null=True)
    


    def _str_(self):
        return self.name