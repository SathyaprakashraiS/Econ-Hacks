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
# Create your views here.
def disease(request):
	form=DiseaseForm(request.POST)
	patientname=Patientname.objects.all()
	context={
		'form':form,'patientname':patientname
	}
	return render(request,"disease.html",context)

def diseaseans(request):
	cname=request.POST.get("name")
	symptom=request.POST.get("symptom")
	if cname==None:
		print("working")
		return redirect('/disease/')
	search=Diseasetypes.objects.all().filter(patient=cname)
	for i in search:
		if ((SequenceMatcher(None,str(symptom),str(i.symptoms)))>0.6):
			print("match found")
		else:
			print("no match found")
		if symptom in str(i.symptoms):
			print("found")
	context={

	}
	return render(request,"diseaseans.html",context)