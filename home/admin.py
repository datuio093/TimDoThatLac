from django.contrib import admin
from .models import mypost,comment,blog
# Register your models here.

admin.site.register(mypost)
admin.site.register(comment)
admin.site.register(blog)