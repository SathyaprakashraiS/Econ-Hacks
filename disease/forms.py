from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import *

class DiseaseForm(forms.ModelForm):
	"""Form for the image model"""
	class Meta:
		model = Diseasetypes
		fields = ['crop']
