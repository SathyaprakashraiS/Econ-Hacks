from django.shortcuts import render,redirect
from django.http import JsonResponse
from datetime import date
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from difflib import SequenceMatcher
#from .utils import cookieCart, cartData, guestOrder

import json
import datetime
from .models import *
from .forms import *
import difflib
from re import search

# Create your views here.
def disease(request):
	form=DiseaseForm()
	patientname=Patientname.objects.all()
	context={
		'form':form,'patientname':patientname
	}
	return render(request,"disease.html",context)

def diseaseans(request):
	form=DiseaseForm(request.POST)
	#cname=request.POST.get("name")
	symptom=request.POST.get("symptom")
	symptom=symptom.lower()
	if form.is_valid():
		cname=form.cleaned_data['patient']
		#print("this",form.cleaned_data['patient'],"symp",symptom)
		if cname==None:
			print("working")
			return redirect('/disease/')
		searchqry=Diseasetypes.objects.all().filter(patient=cname)
		suspect=Diseasetypes.objects.all().filter(patient=cname)
		#search=Diseasetypes.objects.values_list('symptoms')
		for i in searchqry:
			temp=str(i.symptoms)
			temp=temp.lower()
			if len(temp)>len(symptom):
				if search(symptom,temp):
					print ("Found!")
					print("ratio:",difflib.SequenceMatcher(None,symptom,temp).ratio())
				else:
					suspect=suspect.exclude(symptoms=i.symptoms)
					print("Not found!0")
					print("ratio:",difflib.SequenceMatcher(None,symptom,temp).ratio())
			else:
				if search(temp,symptom):
					print ("Found!")
					print("ratio:",difflib.SequenceMatcher(None,symptom,temp).ratio())
				else:
					suspect=suspect.exclude(symptoms=i.symptoms)
					print ("Not found!1")
					print("ratio:",difflib.SequenceMatcher(None,symptom,temp).ratio())
	context={
		'suspect':suspect
	}
	return render(request,"diseaseans.html",context)