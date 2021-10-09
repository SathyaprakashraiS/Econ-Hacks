from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model
from store.models import *
from city.models import *
from .models import *
from django.db.models.functions import Lower
from itertools import chain
from django.db.models import F

# Create your views here.
def restrictionfinder(request):
	dboycity=request.user.city
	linkgen1=Orderer.objects.values_list('add1link')
	linkgen2=Orderer.objects.values_list('add2link')
	dlist=Orderer.objects.all().filter(city=dboycity.lower())
	testlist=Orderer.objects.all().filter(city=dboycity.lower())
	clist=Area.objects.all().filter(city__name=dboycity.lower())
	alist=Orderer.objects.all().filter(city=dboycity.lower())
	vacdno=request.user.vacinated
	pervaikala=[]
	for string in clist:
		obj=[]
		alist=alist.filter(address2__contains=string)
		obj=Area.objects.all()
		obj=obj.filter(areaname__contains=string)
		if testlist.filter(address2__contains=string):
			testlist.filter(address2__contains=string).update(reslev=string.restrictionlevel)
			testlist.filter(address2__contains=string).update(omaplink=string.maplink)
	listreslev1=Orderer.objects.all().filter(city=dboycity.lower(),reslev__lte=1,done=0)
	listreslev2=Orderer.objects.all().filter(city=dboycity.lower(),reslev__lte=2,done=0)
	listreslev3=Orderer.objects.all().filter(city=dboycity.lower(),reslev__lte=3,done=0)
	lor=City.objects.all().filter(name=dboycity.lower())
	result=list(chain(dlist,pervaikala))

	'''
	
	result=list(chain(obj,pal,veg,vag,ket,med))


	dboycity=request.user.city
	dlist=Orderer.objects.all().filter(city=Lower(dboycity))
	lor=City.objects.all()
	'''
	return render(request,'delivery.html',{'dboycity':dboycity,'dlist':dlist,'lor':lor,'linkgen1':linkgen1,'linkgen2':linkgen2,'vacdno':vacdno,'alist':alist,'result':result,'testlist':testlist,'listreslev1':listreslev1,'listreslev2':listreslev2,'listreslev3':listreslev3})

def unidel(request):
	a = request.POST.get('custom')
	obj = Orderer.objects.filter(pk__exact=a)
	level=Orderer.objects.values_list('reslev').filter(pk__exact=a)
	return render(request,'unidel.html',{'obj':obj,'level':level})

def modifyasdelivered(request):
	a = request.GET['custom']
	obj = Orderer.objects.filter(pk__exact=a)
	obj=obj.update(done=3)
	return HttpResponseRedirect("/delivery")

def modifyasfake(request):
	a = request.GET['custom']
	obj = Orderer.objects.all().filter(pk__exact=a)
	scammail=Orderer.objects.values_list('email').filter(pk__exact=a)
	scammed=list(Orderer.objects.values_list('email').filter(pk__exact=a))
	print("scammail:",scammail)
	Usersq=get_user_model()
	scammer=Usersq.objects.values_list('email')
	for i in scammer:
		for j in scammail:
			if i==j:
				Usersq.objects.filter(email=str(i)[2:-3]).update(merit=F('merit')-10)
				obj=obj.update(done=1)
	return HttpResponseRedirect("/delivery")

def modifyasNA(request):
	a = request.GET['custom']
	obj = Orderer.objects.filter(pk__exact=a)
	obj=obj.update(done=1)
	return HttpResponseRedirect("/delivery")