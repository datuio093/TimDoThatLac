from django import forms
from .models import *

class imgpost(forms.ModelForm):

    class Meta:
        model = mypost
        fields = ['images']
