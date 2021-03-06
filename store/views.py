from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from .forms import OrdererForm
from datetime import date
from django.contrib import messages
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect

def viewprofile(request):
    
    if request.method == 'POST':
              e_form = CustomUserForm(request.POST,instance=request.user)
             
        
              if e_form.is_valid():
                  e_form.save()
              
                  messages.success(request,f'your account has been updated!')
                  return redirect('dispprofile')
    else:
        e_form = CustomUserForm(instance=request.user)
          
    context ={
        'e_form':e_form,

    }
    return render(request,"dbedit.html",context)

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all().filter(veg=True,approval=True)
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)
	email=request.user.email
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	score=request.user.merit
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	if request.method == 'POST':
		form = OrdererForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/delivery",{'form':form})
	else:
		form = OrdererForm()

	context = {'items':items,'score':score, 'order':order, 'cartItems':cartItems,'form': form}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

def orderhistory(request):
	uemail=request.user.email
	obj=Orderer.objects.all().filter(email=uemail,done=3)
	cobj=Orderer.objects.all().filter(email=uemail,done__lte=2)
	return render(request,'ohistory.html',{'uemail':uemail,'obj':obj,'cobj':cobj})

def agroprod(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.all().filter(veg=False,approval=False)
	
	context={
		'products':products, 'cartItems':cartItems
	}
	return render(request,"agroprod.html",context)

def addprod(request):
	form=AgroprodForm()
	context={
		'form':form
	}
	return render(request,"addprod.html",context)

def submitprod(request):
	form=AgroprodForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		messages.success(request, "Thank you! You have successfully added your product!")
		return HttpResponseRedirect('/store/')
	else:
		messages.failure(request, "Error! product was not added !")
		return HttpResponseRedirect('/store/addprod')
