from django.db import models

# Create your models here.
class Patientname(models.Model):
	name=models.CharField(max_length=100)

class Diseasetypes(models.Model):
	dname=models.CharField(max_length=50,default="deisease name")
	symptoms=models.CharField(max_length=200,default="_")
	patient=models.ForeignKey(Patientname,on_delete=models.CASCADE)