from django.db import models

# Create your models here.
class News(models.Model):
	name=models.CharField(max_length=100,default="headline")
	link=models.CharField(max_length=1000,default="#")
	img=models.ImageField(upload_to='images',default='static/images/default.jpg')