from django.db import models

# Create your models hereeee.
class mypost(models.Model):
    title = models.TextField()
    type = models.TextField()
    object = models.TextField()
    descrip = models.TextField()
    address = models.TextField()
    name = models.TextField()
    pnum = models.TextField()
    email = models.TextField()


    def _str_(self):
        return self.name