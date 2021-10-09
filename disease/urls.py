from django.urls import path,include
from . import views

urlpatterns = [
	path('',views.disease, name="disease"),
	path('diseaseans/',views.diseaseans, name="diseaseans"),
]