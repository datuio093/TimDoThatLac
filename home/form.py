
from django import forms
from .models import *

class images(forms.ModelForm):

    class Meta:
        model = mypost
        fields = ['image']
