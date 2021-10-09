from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Orderer,CustomUser

class CustomUserForm(forms.ModelForm):
     """Form for the image model"""
     class Meta:
        model = CustomUser 
        fields ='__all__'


class OrdererForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
       model = Orderer
       fields = ('name','email','address1','address2','city','state','zipcode','country','landmark','count','quantity','customerhousetype','contactno','paymode')
		