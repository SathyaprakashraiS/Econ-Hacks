from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('news/', views.news, name="news"),
	path('tips/', views.tips, name="tips")
]