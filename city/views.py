from django.shortcuts import render
#from store.models import Orderer
#from deliveryperson.models import Persondetails
from .models import *

# Create your views here.
'''
def restrictionfinder(request):
	dmcity=request.user.city
	obj=Orderer.object.all().filter(city=dmcity)
	return render(request,'delivery.html',{'obj':obj,'dmcity':dmcity})
'''