from django.db import models
from .models import *

# Create your models hereeee.
class mypost(models.Model):
    user = models.TextField(null=True)
    title = models.TextField(max_length=1000)
    type = models.TextField()
    object = models.TextField()
    descrip = models.TextField(max_length=10000000)
    address = models.TextField()
    name = models.TextField(max_length=1000)
    pnum = models.IntegerField(null=True, blank=True)
    email = models.TextField(max_length=1000)
    images = models.ImageField(null=True ,blank=True , upload_to='images/')


    def _str_(self):
        return self.name