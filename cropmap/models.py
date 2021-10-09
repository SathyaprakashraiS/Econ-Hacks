from django.db import models
import geocoder

# Create your models here.

class Croplist(models.Model):
   crop = models.CharField(max_length=25,default="cropname")
   crop_img = models.URLField()
   state = models.CharField(max_length=15,default="indian state")
   lat = models.FloatField(default=0)
   log = models.FloatField(default=0)


   def save(self,*args,**kwargs):
       self.lat = geocoder.osm(self.state).lat
       self.log = geocoder.osm(self.state).lng
       return super().save(*args,**kwargs)

   def __str__(self):
       return self.state

