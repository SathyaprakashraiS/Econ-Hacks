from django.shortcuts import render
from django.http import JsonResponse
from datetime import date
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
#from .utils import cookieCart, cartData, guestOrder

import json
import datetime
from .models import *

# Create your views here.
def home(request):
	return render(request,"home.html",{})

def news(request):
	news=News.objects.all()
	context={
		'news':news
	}
	return render(request,"news.html",context)