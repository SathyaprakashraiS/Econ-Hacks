from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def vacform(request):
	if request.method == 'POST':
		form = VacForm(request.POST,request.FILES)
		if form.is_valid():
			#user.formsubmitted.update(formsubmitted=True)
			print("here")
			form.save()
			messages.success(request, "Thank you! Your Vaccine form is submitted is pending for approval!")
			return HttpResponseRedirect('/')
	else:
		form = VacForm()

	return render(request,"vacform.html",{'form':form})