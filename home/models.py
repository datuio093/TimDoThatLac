from django.db import models
from .models import *

# Create your models hereeee.
class mypost(models.Model):
    title = models.TextField(max_length=1000)
    type = models.TextField()
    object = models.TextField()
    descrip = models.TextField(max_length=10000000)
    address = models.TextField()
    name = models.TextField(max_length=1000)
    pnum = models.IntegerField()
    email = models.TextField(max_length=1000)


    def _str_(self):
        return self.name