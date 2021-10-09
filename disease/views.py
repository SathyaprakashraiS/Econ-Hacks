from django.shortcuts import render
from django.http import JsonResponse
from datetime import date
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
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
	else:
		print(cname,symptom)
	context={

	}
	return render(request,"diseaseans.html",context)