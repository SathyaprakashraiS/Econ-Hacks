from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Vform

class VacForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
       model = Vform
       fields = ('name','vacday','dosecount','prooffile')