from django.db import models
# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=200, null=True)
	def __str__(self):
		return "%s" % (self.name)
	'''
	1>low cases
	2>medium cases
	3>high cases
	'''

class Area(models.Model):
	city = models.ForeignKey(City,on_delete=models.CASCADE)
	areaname = models.CharField(max_length=200, null=True)
	restrictionlevel=models.FloatField(default=1)
	maplink=models.CharField(max_length=1000,default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.001696423075!2d79.15722781561198!3d12.971742990855768!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bad479f0ccbe067%3A0xfef222e5f36ecdeb!2sVellore%20Institute%20of%20Technology!5e0!3m2!1sen!2sin!4v1628800616114!5m2!1sen!2sin')
	
	def __str__(self):
    	 return self.areaname
	class Meta:
		 ordering = ['areaname']

'''
class City(models.Model):
	name = models.CharField(max_length=200, null=True)
	restrictionlevel=models.FloatField(default=1)
	''
	''
	1>low cases
	2>medium cases
	3>high cases
	'''
