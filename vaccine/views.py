from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def vacform(request):
	if request.method == 'POST':
		form = VacForm(request.POST,request.FILES)
		if form.is_valid():
			user.formsubmitted.update(formsubmitted=True)
			form.save()
			return render(request, 'main.html', {'form': form})
	else:
		form = VacForm()

	return render(request,"vacform.html",{'form':form})