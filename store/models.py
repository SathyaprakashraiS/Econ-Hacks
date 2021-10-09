from django.db import models
from ecommerce import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Lower

# Create your models here.
User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    is_dboy = models.BooleanField(default=False)
    city =models.CharField(max_length=10,default='city')
    formsubmitted = models.BooleanField(default=False)
    vacinated = models.IntegerField(default=0)
    merit=models.IntegerField(default=100)
# Create your models here.

class Orderer(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	address1 = models.CharField(max_length=200,default="addressl line 1")
	add1link = models.CharField(max_length=200,default="addressl line 1")
	address2 = models.CharField(max_length=200,default="addressl line 2")
	add2link = models.CharField(max_length=200,default="addressl line 2")
	city = models.CharField(blank=True,max_length=200)
	state = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	landmark=models.CharField(max_length=500,default="direction from home to nearest Landmark")
	count=models.FloatField(default=0)
	quantity=models.FloatField(default=0)
	customerhousetype=models.CharField(max_length=5,default='1')
	reslev=models.FloatField(default=2)
	omaplink=models.CharField(max_length=1000,default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.001696423075!2d79.15722781561198!3d12.971742990855768!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bad479f0ccbe067%3A0xfef222e5f36ecdeb!2sVellore%20Institute%20of%20Technology!5e0!3m2!1sen!2sin!4v1628800616114!5m2!1sen!2sin",null=True)
	done=models.CharField(max_length=5,default=0)
	contactno=models.CharField(max_length=10,default="test")
	paymode=models.CharField(max_length=5,default='1')	

	def save(self,*args,**kwargs):
		self.city=self.city.lower()
		self.add1link=self.address1.replace(",",",+")
		self.add1link=self.add1link.replace(" ","+")
		self.add2link=self.address2.replace(",",",+")
		self.add2link=self.add2link.replace(" ","+")
		super().save(*args,**kwargs)

	def __str__(self):
		return (self.name)

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.user.username
		
def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile = Customer.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address